import asyncio
from models import Author, Post
from tortoise import Tortoise

DB = "sqlite://dev.db"


async def init():
    await Tortoise.init(db_url=DB, modules={"models": ["models"]}) 
    await Tortoise.generate_schemas()


async def _get_authors():
    authors = await Author.all()
    return authors


def get_authors():
    authors = asyncio.run(_get_authors())
    return authors


async def _get_posts():
    posts = await Post.all()
    return posts


def get_posts():
    posts = asyncio.run(_get_posts())
    return posts


if __name__ == "__main__":
    from tortoise import run_async
    run_async(init())
