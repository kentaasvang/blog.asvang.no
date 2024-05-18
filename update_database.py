from tortoise import Tortoise


async def update_database():
    await Tortoise.init()
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    from tortoise import run_async
    run_async(update_database())
