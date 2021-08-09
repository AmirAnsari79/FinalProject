from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    prepopulated_fields = {'Slug': ('Name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Available',)
    list_filter = ('Available',)
    list_editable = ('Price', 'Available')
    prepopulated_fields = {'Slug': ('Name', 'Price')}
    raw_id_fields = ('Category',)
    actions = ('AvailableAction',)

    def AvailableAction(self, request, queryset):
        queryset.update(Available=True)

    AvailableAction.short_description = 'access available'
