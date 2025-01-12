from django.contrib import admin
from .models import Topic, Post, Comment, Report
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Report)