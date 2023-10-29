import os
import requests
from datetime import datetime
from loguru import logger


def get_weather(city: str = None):

    token = str(os.environ["OPEN_WEATHER_TOKEN"])

    # Обрабатываем полученное название города
    city = city.title().strip()

    # Формируем url
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={token}"

    # Отправляем запрос
    response = requests.get(url=url)
    logger.info(f"Запрос погоды для города: {city}")

    if response.status_code != 200:
        result = 'Указанный город не найден'
        logger.error(f'Указанный в запросе город ({city}) не найден')
    else:
        response = response.json()
        logger.info(f"Получен ответ на запрос для города: {city}")

        # Вычисляем временные переменные
        sunrise = datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset = datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])
        current_time = datetime.fromtimestamp(response['dt'] + response['timezone'])

        # Формируем результат
        result = (f"Температура: {response['main']['temp']}℃.\n"
                  f"Ощущается: {response['main']['feels_like']}℃.\n"
                  f"{response['weather'][0]['description'].capitalize()}.\n"
                  f"Ветер: {response['wind']['speed']} м/с.\n"
                  f"Влажность: {response['main']['humidity']}%.\n"
                  f"Время измерения (местное): {current_time.strftime('%H:%M')}.\n"
                  f"Рассвет: {sunrise.strftime('%H:%M')}.\n"
                  f"Закат: {sunset.strftime('%H:%M')}")

    return result
