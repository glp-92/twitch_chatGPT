# Twitch ChatGPT BOT

This repository allows you to associate a chatbot usable in a Twitch channel chat using the OpenAI API.

## Current version of ChatGPT in use: gpt-3.5-turbo

### Prerequisites:
- OpenAI API Token: Registration on their platform is required [https://platform.openai.com/signup](https://platform.openai.com/signup)
- Twitch Token: Required for use with IRC; requires logging in with a Twitch account [https://twitchtokengenerator.com/](https://twitchtokengenerator.com/)

### Execution Requirements:
- Python 3.10 (includes switch - case instruction)

### Environment Variables

| VAR | VALUE | DESC |
| --- | --- | --- |
| GPT_ENDPOINT | https://api.openai.com/v1/chat/completions | OpenAI API Endpoint |
| GPT_TOKEN | Bearer xx | OpenAI Token for registered account |
| TWITCH_IRC_SERVER | irc.chat.twitch.tv | Twitch IRC URL |
| TWITCH_IRC_PORT | 6667 | Twitch IRC Port |
| TWITCH_IRC_NICKNAME | xx | Nickname of the account used as a bot |
| TWITCH_TOKEN | oauth:xx | Token of the account used as a bot |
| CHANNEL_MONITORING | #xx | Channel name to monitor preceded by '#' |

### Exec:
``` 
cd src/  
python3 main.py
```
