# Twitch ChatGPT Bot

This repository provides a Twitch chatbot that leverages the OpenAI API.

## Current version: gpt-3.5-turbo


### Prerequisites:

- OpenAI API Token: Sign up on their platform [here](https://platform.openai.com/signup)
- Twitch Token: Login with your Twitch account and generate a token [here](https://twitchtokengenerator.com/)


### Execution Requirements:

- Python 3.10 (includes `switch`-`case` instruction)


### Environment Variables:

| Variable | Value | Description |
| --- | --- | --- |
| GPT_ENDPOINT | https://api.openai.com/v1/chat/completions | OpenAI API endpoint |
| GPT_TOKEN | Bearer xx | Token for your registered OpenAI account |
| TWITCH_IRC_SERVER | irc.chat.twitch.tv | Twitch IRC URL |
| TWITCH_IRC_PORT | 6667 | Twitch IRC port |
| TWITCH_IRC_NICKNAME | xx | Nickname of the account used as a bot |
| TWITCH_TOKEN | oauth:xx | Token for the account used as a bot |
| CHANNEL_MONITORING | #xx | Name of the channel to monitor, preceded by '#' |


### Execution:
``` 
cd src/  
python3 main.py
```


### How to prompt on Twitch chat:

To be able to prompt on Twitch chat, the program needs to be running and the connection with IRC must be established.

The format to make prompts is the following:

``` 
!chat inputPrompt
```

If there are no errors, the bot will answer the prompt quoting the transmitter.

If you want to change the number of characters the GPT will answer, you can do it in the gpt.py file in the send_request function, where a limit of 150 characters is specified.

`gpt.py`
```
def send_request(self, prompt, limit = 150):
```


### Future Optimizations:

- Implementation of prompt queue to be resolved by the GPT.
- Multithreading to monitor multiple Twitch channels simultaneously.