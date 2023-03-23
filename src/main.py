'''
Created on 23 mar. 2023

@author: Guille
@comment: gpt API integrated on python
'''

import os
from twitch_bot import twitch_BOT


with open('.env') as f:
    for line in f:
        # Si la línea empieza con "#" es un comentario y se salta
        if line.startswith('#'):
            continue
        # Separar la línea en clave y valor
        key, value = line.strip().split('=', 1)
        # Configurar la variable de entorno
        os.environ[key] = value


data = {
    'gpt': {
        'endpoint': os.environ.get('GPT_ENDPOINT'),
        'token': os.environ.get('GPT_TOKEN')
    },
    'twitch_bot': {
        'server': os.environ.get('TWITCH_IRC_SERVER'),
        'port': os.environ.get('TWITCH_IRC_PORT'),
        'nickname': os.environ.get('TWITCH_IRC_NICKNAME'),
        'token': os.environ.get('TWITCH_TOKEN'),
        'channel_to_monitor': os.environ.get('CHANNEL_MONITORING')
    }
}


twitch_bot = twitch_BOT(data)
twitch_bot.run()