from django.contrib import admin
from . import models as account_models


@admin.register(account_models.User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'is_staff', 'is_active')
