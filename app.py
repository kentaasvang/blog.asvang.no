import asyncio
from flask import Flask, render_template
from models import Author
from db import init, get_posts
from tortoise import run_async

run_async(init())

app = Flask(__name__)


@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

