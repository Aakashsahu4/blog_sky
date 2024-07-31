from django.contrib import admin
from . import models as blog_model


@admin.register(blog_model.Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','user_profile', 'content')


@admin.register(blog_model.Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('from_user','to_user','blog','read')