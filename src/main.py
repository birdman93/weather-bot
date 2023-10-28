from bot import telegram_bot


if __name__ == '__main__':

    bot = telegram_bot()

    while True:

        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as ex:
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')
