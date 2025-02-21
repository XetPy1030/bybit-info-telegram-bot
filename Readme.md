# Bybit info telegram-bot

## Описание

Бот для получения информации о балансе Bybit.

## Команды

/start - начать работу с ботом
/balance - получить информацию о балансе
/set_secret_key - установить secret_key и дату истечения
/expires_at - проверить когда истекает secret_key

## Установка

1. Установить зависимости
    ```bash
    pip install poetry
    poetry install
    ```

2. Скопировать `.env.example` в `.env` и заполнить переменные окружения

3. Запустить docker-compose
    ```bash
    docker compose up -d
    ```

## Настройка secret_key для запросов к Bybit (из cookies - secret_key)

1. Зайти на [Bybit](https://www.bybit.com/)
2. Через F12 найти cookie `secret_key`
3. Скопировать значение cookie `secret_key`
4. После запуска бота ввести команду `/set_cookie` и ввести значение cookie `secret_key`
