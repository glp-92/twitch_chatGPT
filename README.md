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
