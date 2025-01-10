from django.contrib import admin
from .models import Topic, Post, Comment, Report

# Register your models here.
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Report)