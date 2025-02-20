from app.config import PostgresConfig

TORTOISE_ORM = {
    "connections": {"default": {
        "engine": "tortoise.backends.asyncpg",
        "credentials": {
            "host": PostgresConfig.HOST,
            "port": PostgresConfig.PORT,
            "user": PostgresConfig.USER,
            "password": PostgresConfig.PASSWORD,
            "database": PostgresConfig.DB,
        }
    }},
    "apps": {
        "models": {
            "models": ["app.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
