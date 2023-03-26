'''
Created on 13 jun. 2022

@author: Guille
@comment: Twitch Bot Class using Sockets
'''


import socket, time
from gpt import gpt


class twitch_BOT():


    def __init__(self, data):
        self.irc_server = data['twitch_bot']['server']
        self.port = data['twitch_bot']['port']
        self.token = data['twitch_bot']['token']
        self.nickname = data['twitch_bot']['nickname']
        self.channel_to_monitor = data['twitch_bot']['channel_to_monitor']
        self.gpt_chat = gpt(data)
        self.command_flag = False


    def sock_create(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        
    def connect_to_irc(self):
        try:
            self.s.connect((self.irc_server, int(self.port)))
            self.s.send(f"PASS {self.token}\n".encode('utf-8'))
            self.s.send(f"NICK {self.nickname}\n".encode('utf-8'))
            self.s.send(f"JOIN {self.channel_to_monitor}\n".encode('utf-8'))
            print(f"Socket stablished with IRC:: {self.channel_to_monitor}")
            #self.s.settimeout(5)
        except Exception as e:
            print(f"Error stablishing socket with IRC:: {e}")


    def listen_irc(self):
        def capture_irc_answer():
            if irc_answer == "": raise
            match(irc_answer.find('PRIVMSG')):
                case -1:
                    print(f"Message from IRC {irc_answer}")
                case _:
                    text_to_capture = f".tmi.twitch.tv PRIVMSG {self.channel_to_monitor} :"
                    usr_str, msg_str = irc_answer.split(text_to_capture)
                    _, usr = usr_str.split('@')
                    msg_str = msg_str[:-2]
                    print(f"Message from usr => {usr}: {msg_str}")
                    if "!chat" in msg_str:
                        response = f"@{usr}: "
                        try:
                            response += self.gpt_chat.send_request(msg_str.split("!chat")[-1])
                            success = self.send_chat_message(response)
                        except Exception as e:
                            print(f"Error sending prompt to GPT => {e}")
            return

        while True:
            try:
                irc_answer = self.s.recv(2048).decode('utf-8')
                if irc_answer.startswith('PING'):
                    self.s.send("PONG\n".encode('utf-8'))
                else:
                    capture_irc_answer()
            except TimeoutError:
                continue
            except Exception as e:
                print(f"Error on listening server: {e}")
                break
            time.sleep(0.1)


    def run(self):
        while True:
            self.sock_create()
            self.connect_to_irc()
            self.listen_irc()
            time.sleep(0.1)
        

    def send_chat_message(self, message_to_send: str) -> bool:
        try:
            print(f"Sending message => {message_to_send}")
            message_coded = (f"PRIVMSG {self.channel_to_monitor} :{message_to_send}\r\n").encode('utf-8')
            self.s.send(message_coded)
            success = True
        except Exception as e:
            print(f"Error on sending message to server: {e}")
            success = False
        return success


    def set_command_flag(self, state):
        self.command_flag = state