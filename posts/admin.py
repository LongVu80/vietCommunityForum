from django.contrib import admin
from .models import Post, Image, Comment, Reply, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Reply)
