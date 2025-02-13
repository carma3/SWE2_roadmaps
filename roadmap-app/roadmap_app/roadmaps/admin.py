from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Create admin that can manage the AppUser and add the relevant field (role)

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

admin.site.register(AppUser, CustomUserAdmin)