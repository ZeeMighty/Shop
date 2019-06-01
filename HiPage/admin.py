from django.contrib import admin
from HiPage.models import Good, Size

class Sizes(admin.TabularInline):
    model = Size
    extra = 1

class GoodAdmin(admin.ModelAdmin):
    model = Good
    list_display = ('Name', 'Available')
    list_filter = ['id']
    search_fields = ['Name']
    fieldsets = [
    ('Name', {'fields': ['Name']}),
    ('Available', {'fields': ['Available']}),
    ('Photo', {'fields': ['Photo'], 'classes': ['collapse']})
    ]
    inlines = [Sizes]

admin.site.register(Good, GoodAdmin)
