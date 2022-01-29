from django.contrib import admin
from .models import Tag, Snippet, Comment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Snippet)
admin.site.register(Comment)
