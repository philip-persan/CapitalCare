from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações do Usuário", {"fields": (
            "phone",
        )}),
    )
