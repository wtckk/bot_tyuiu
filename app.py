async def on_startup(dp):
    import filters
    filters.setup(dp)
    from loader import db

    import middlewares
    middlewares.setup(dp)

    from utils.db_api.db_gino import on_startup
    print('[INFO] Подключение к PostgreSQL')

    await on_startup(dp)

    print("[INFO] Создание таблиц")
    await db.gino.create_all()

    from utils.notify_admins import on_startup_notify

    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands

    await set_default_commands(dp)

    print("[INFO] Bot started.")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
