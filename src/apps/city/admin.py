from apps.city.models import City
from django.contrib import admin


class CityAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)
