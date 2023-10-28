# Используем базовый образ Python
FROM python:3

# Переменные окружения
ENV OPEN_WEATHER_TOKEN="b49e0a95ef766db6c5ce33e84098e2b5"
ENV WEATHER_BOT_TOKEN="6851139190:AAHjgOrmoT5RRzY5sPLfW5bpiQ_N0zsGX2Y"

# Создайте и установите виртуальное окружение
RUN python -m venv /venv

# Скопируйте все файлы из вашего текущего каталога в контейнер
COPY . /

# Активируйте виртуальное окружение
SHELL ["/bin/bash", "-c"]
RUN source /venv/bin/activate

# Установите зависимости
RUN pip install -r /reqs.txt

# Запустите ваш Python скрипт
CMD ["python", "/src/main.py"]
