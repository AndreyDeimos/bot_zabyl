# Project "Забыл" Telegram Bot

A Telegram bot for the "Забыл" project that helps users manage their tasks and reminders.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Telegram bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

## Features

- Welcome message with interactive keyboard
- Project information
- Participation instructions
- Error handling and logging

## Development

The bot is built using:
- Python 3.7+
- pyTelegramBotAPI
- python-dotenv for environment variable management

## Security

Never commit your `.env` file or expose your bot token. The `.env` file is already included in `.gitignore`.
