from django.contrib import admin
from Blog.models import *
# Register your models here.
"""
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc',)
    list_display_links = ('title','desc',)

    fieldsets = (
        (None,{
            'fields':('title','desc','content','category','tags',)
        }),

    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
"""
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
