from django.contrib import admin
from musicapp.models import Tracks, Tour, Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Customize django admin


class MyUserAdmin(BaseUserAdmin):
    list_display = (
        'email', 'date_joined', 'last_login', 'is_admin', 'is_active'
    )
    search_fields = (
        'email', 'username'
    )
    readonly_fields = (
        'date_joined', 'last_login'
    )
    filter_horizontal = (

    )
    list_filter = ('last_login',)

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','username','first_name','last_name','password1','password2'),
        }),
    )

    ordering = ('email',)


# Register your models here.
admin.site.register(Tracks)
admin.site.register(Tour)
admin.site.register(Account, MyUserAdmin)
