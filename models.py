from tortoise.models import Model
from tortoise import fields


class Author(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    body = fields.TextField()
    thumbnail_url = fields.CharField(max_length=255, null=True)
    
