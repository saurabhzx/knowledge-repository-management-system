from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'last_login', 'date_joined')
    list_display_links = ('username', )
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
