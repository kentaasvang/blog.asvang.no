from models import Post
from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from tortoise.contrib.starlette import register_tortoise

DB_URL = "sqlite://dev.db"

app = Starlette() 
templates = Jinja2Templates(directory="templates")


@app.route("/", methods=["GET"])
async def index(request):
    posts = await Post.all() 
    return templates.TemplateResponse(request, "index.html", context={"posts": posts})


register_tortoise(app, db_url=DB_URL, modules={"models":["models"]})
