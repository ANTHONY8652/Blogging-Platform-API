from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = UserAdmin
    list_display = ['username', 'email', 'is_staff', 'is_active', 'created_at', 'updated_at']
    search_fields = ['username', 'email']
    ordering = ['username', 'email']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','is_staff', 'is_active')
        }),
    )

admin.site.register(User, CustomUserAdmin)

# Register your models here.