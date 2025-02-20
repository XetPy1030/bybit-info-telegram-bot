FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Установка рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY pyproject.toml poetry.lock ./

# Настройка Poetry и установка зависимостей
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копирование исходного кода
COPY . .

# Команда по умолчанию
CMD ["poetry", "run", "python", "main.py"]
