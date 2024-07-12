from apps.advert.models import Advert
from django.contrib import admin


class AdvertAdmin(admin.ModelAdmin):
    pass


admin.site.register(Advert, AdvertAdmin)
