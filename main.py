import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup
from env import API_TOKEN

bot = AsyncTeleBot(API_TOKEN)

markup_keyboard = ReplyKeyboardMarkup()
markup_keyboard.add("Что такое проект 'Забыл'?")
markup_keyboard.add("Как участвовать в проекте 'Забыл'?")


async def welcome_message(message):
    await bot.send_message(
        message.chat.id,
        "Добро пожаловать в проект 'Забыл'!",
        reply_markup=markup_keyboard,
    )


async def message_handler(message):
    await bot.send_message(message.chat.id, "Забыл")


bot.register_message_handler(welcome_message, commands=["start"])
bot.register_message_handler(message_handler, func=lambda message: True)

asyncio.run(bot.polling())
