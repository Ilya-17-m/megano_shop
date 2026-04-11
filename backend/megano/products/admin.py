from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import ProductModel, ImagesModel, TagsModel, ReviewModel, SpecificationsModel, CategoriesModel, SubcategoriesModel


@admin.register(CategoriesModel)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title',
    list_display_links = 'pk', 'title',
    search_fields = 'title',
    fieldsets = [
        (None, {
            'fields': ('title', 'image', 'subcategories')
        }),
    ]


@admin.register(SubcategoriesModel)
class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title',
    list_display_links = 'pk', 'title',
    search_fields = 'title',
    fieldsets = [
        (None, {
            'fields': ('image', 'title')
        }),
    ]


@admin.register(SpecificationsModel)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'value'
    list_display_links = 'pk', 'name', 'value'
    search_fields = 'name', 'value'
    fieldsets = [
        (None, {
            'fields': ('name', 'value')
        }),
    ]


@admin.register(ReviewModel)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'author', 'email', 'rate',
    list_display_links = 'pk', 'author'
    search_fields = 'author', 'email', 'text'
    fieldsets = [
        (None, {
            'fields': ('author', 'email', 'rate', 'text', 'product')
        }),
    ]


@admin.register(ImagesModel)
class ImagesAdmin(admin.ModelAdmin):
    list_display = 'pk', 'alt'
    list_display_links = 'pk', 'alt'
    search_fields = 'alt', 'src'
    fieldsets = [
        (None, {
            'fields': ('src', 'alt')
        }),
    ]


@admin.register(TagsModel)
class TagsAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'
    search_fields = 'name',
    fieldsets = [
        (None, {
            'fields' : ('name',)
        })
    ]


@admin.action(description='Free delivered')
def free_delivered(queryset:QuerySet, request:HttpRequest):
    queryset.update(freeDelivery=True)


@admin.action(description='Not free delivered')
def unfree_delivered(queryset:QuerySet, request:HttpRequest):
    queryset.update(freeDelivery=False)


@admin.action(description='Limited version')
def limited_version(queryset:QuerySet, request:HttpRequest):
    queryset.update(limited_version=True)


@admin.action(description='Unlimited version')
def unlimited_version(queryset:QuerySet, request:HttpRequest):
    queryset.update(limited_version=False)


@admin.action(description='Popular version')
def popular_version(queryset:QuerySet, request:HttpRequest):
    queryset.update(limited_version=True)


@admin.action(description='Unpopular version')
def unpopular_version(queryset:QuerySet, request:HttpRequest):
    queryset.update(limited_version=False)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = 'pk', 'title', 'price', 'count'
    list_display = 'pk', 'title', 'price', 'count',
    search_fields = 'title', 'price', 'count'
    actions = [
        free_delivered,
        unfree_delivered,
        limited_version,
        unlimited_version,
        popular_version,
        unpopular_version,
    ]


    fieldsets = [
        (None, {
            'fields': ('images', 'title', 'count', 'price', 'available',
                       'description', 'fullDescription', 'popular_version', 'limited_version', 'specifications',
                       )
        }),
        ('Info', {
            'fields': ('rating', 'tags', 'freeDelivery', 'category')
        }),
        ('Sale data',{
            'fields': ('salePrice', 'dateForm', 'dateTo')
        }),

    ]