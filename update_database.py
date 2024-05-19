from tortoise import Tortoise, models

async def update_database(db_url):
    await Tortoise.init(db_url=db_url, modules={"models":["models"]})
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    from starlette.config import Config
    from tortoise import run_async

    config = Config(".env")
    DB_URL = config("DB_URL")

    assert DB_URL != None

    run_async(update_database(DB_URL))
