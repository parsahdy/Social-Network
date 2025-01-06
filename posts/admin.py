from django.contrib import admin

from .models import Post, PostFile



class PostFileInlineAdmin(admin.TabularInline):
    model = PostFile
    fields = ('file', )



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_time')
    inlines = (PostFileInlineAdmin,)



#@admin.register(PostFile)
#class PostAdmmn(admin.ModelAdmin):
    #pass
