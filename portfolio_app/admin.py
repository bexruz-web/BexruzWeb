from django.contrib import admin

from .models import Portfolio, Category
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'link']
    filter_horizontal = ['category']


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category)
