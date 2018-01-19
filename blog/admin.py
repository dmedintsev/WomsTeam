from django.contrib import admin
from .models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    text = ('content',)
    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
