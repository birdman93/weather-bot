from bot import telegram_bot

from loguru import logger


if __name__ == '__main__':

    # Настройка логирования в файл "app.log" с уровнем INFO
    logger.add("app.log", level="INFO")

    bot = telegram_bot()

    while True:

        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as ex:
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')
