from django.contrib import admin

from .models import Post, PostFile



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostFile)
class PostAdmmn(admin.ModelAdmin):
    pass
