from django.contrib import admin
from . models import Account


class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('parent','highlighted')


admin.site.register(Account, AccountAdmin)
