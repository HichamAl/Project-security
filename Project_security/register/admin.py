from django.contrib import admin
from .models import VerifiedUsers
# Register your models here.


class VerifiedUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified')
    list_filter = ('verified',)
    search_fields = ('user__username',)

admin.site.register(VerifiedUsers, VerifiedUsersAdmin)

