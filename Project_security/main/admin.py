from django.contrib import admin
from .models import VertrouwdePersonen

# Register your models here.

class VertrouwdePersonenAdmin(admin.ModelAdmin):
    list_display = ('bsn_nummer', 'voornaam', 'achternaam')


admin.site.register(VertrouwdePersonen, VertrouwdePersonenAdmin)