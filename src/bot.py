from weather import get_weather

import os
import telebot


def telegram_bot():

    token = str(os.environ["WEATHER_BOT_TOKEN"])

    bot = telebot.TeleBot(token)

    start_text = "Напишите название города для получения прогноза погоды"

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.from_user.id,
                         start_text,
                         parse_mode='Markdown')

    @bot.message_handler(content_types=['text'])
    def weather(message):

        city = message.text
        forecast = get_weather(city=city)

        bot.send_message(message.from_user.id, forecast)

    return bot
