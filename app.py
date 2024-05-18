from models import Post
import utils
from starlette.config import Config
from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from tortoise.contrib.starlette import register_tortoise


config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
DB_URL = config("DB_URL")


if DEBUG:
    utils.add_query_logging()


app = Starlette(debug=DEBUG) 
templates = Jinja2Templates(directory="templates")


@app.route("/", methods=["GET"])
async def index(request):
    posts = await Post.all() 
    return templates.TemplateResponse(request, "index.html", context={"posts": posts})


register_tortoise(app, db_url=DB_URL, modules={"models":["models"]})
