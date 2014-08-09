from django.contrib import admin
from .models import Section
from .models import Item



class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_search = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'section']
    list_search = ['name']
    list_filter = ('section__name', )

admin.site.register(Section, SectionAdmin)
admin.site.register(Item, ItemAdmin)
