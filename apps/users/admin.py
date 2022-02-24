from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from apps.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name',  'last_name', 'is_staff', 'is_client', 'is_admin', 'is_verified')
    list_filter = ('is_client', 'is_staff', 'is_admin', 'created_at', 'updated_at')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'biography')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('sex', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, CustomUserAdmin)