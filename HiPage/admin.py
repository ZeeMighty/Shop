from django.contrib import admin
from HiPage.models import Good, Size



class GoodAdmin(admin.ModelAdmin):
    model = Good
    list_display = ('Name', 'Available')
    list_filter = ['id']
    search_fields = ['Name']
    fieldsets = [
    ('Name', {'fields': ['Name']}),
    ('Available', {'fields': ['Available']}),
    ('Photo', {'fields': ['Photo'], 'classes': ['collapse']}),
    ('Discount', {'fields': ['Discount'], 'classes': ['collapse']}),
    ('Price', {'fields': ['Price']}),
    ('Sizes', {'fields': ['Size']}),
    ]

admin.site.register(Good, GoodAdmin)
admin.site.register(Size)
