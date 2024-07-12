from apps.category.models import Category
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
