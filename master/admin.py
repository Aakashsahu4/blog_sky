from django.contrib import admin
from . import models as master_models


@admin.register(master_models.Logo)
class LogoAdmin(admin.ModelAdmin):
	list_display = ['title','file'] 