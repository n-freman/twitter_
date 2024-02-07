from django.contrib import admin

from .models import CustomUser


class CustomUserAdminConfig(admin.ModelAdmin):
    list_display = ['email', 'username', 'date_joined']


admin.site.register(CustomUser, CustomUserAdminConfig)

