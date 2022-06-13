from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('username','phone_number','email','national_id',
                    'date_joined','last_login','is_admin','is_staff','is_active')
    search_fields = ('username','email',)
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
