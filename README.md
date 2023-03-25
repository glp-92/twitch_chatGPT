# Twitch ChatGPT BOT

Este repositorio te permite asociar mediante la API de OpenAI un chatbot utilizable en un chat de un canal de Twitch.

## Versión actual de ChatGPT: gpt-3.5-turbo

### Requisitos previos:
- Token de API OpenAI: Es necesario el registro en su plataforma: [https://platform.openai.com/signup](https://platform.openai.com/signup)
- Token de Twitch: Es necesario para su uso por el IRC; requiere iniciar sesión con una cuenta de Twitch: [https://twitchtokengenerator.com/](https://twitchtokengenerator.com/)

### Requisitos de ejecución:
- Python 3.10 (incluye instrucción switch - case)

### Variables de entorno

| VAR | VALUE | DESC |
| --- | --- | --- |
| GPT_ENDPOINT | https://api.openai.com/v1/chat/completions | Endpoint de API OpenAI |
| GPT_TOKEN | Bearer xx | Token de OpenAI para cuenta registrada |
| TWITCH_IRC_SERVER | irc.chat.twitch.tv | Url de IRC de Twitch |
| TWITCH_IRC_PORT | 6667 | Puerto del IRC de Twitch |
| TWITCH_IRC_NICKNAME | xx | Nick de la cuenta usada como bot |
| TWITCH_TOKEN | oauth:xx | Token de la cuenta usada como bot |
| CHANNEL_MONITORING | #xx | Nombre de canal a monitorizar precedido por '#' |

### Ejecución:
``` 
cd src/  
python3 main.py
```
