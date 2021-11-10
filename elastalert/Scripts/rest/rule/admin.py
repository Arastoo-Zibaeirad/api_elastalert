from django.contrib import admin
from .models import Rule, Query

# Register your models here.

class QueryInline(admin.TabularInline):
    model = Query
class RuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'index_name', 'create_time', 'modified_time', 'query']
    search_fields = ['name', 'index_name', 'create_time', 'modified_time']
    list_display_links = ['name']
    inlines = [QueryInline]


class QueryAdmin(admin.ModelAdmin):
    list_display = ['event_category', 'condition']
    # list_editable = ['sequence']
    search_field = ['event_category', 'condition']


admin.site.register(Rule, RuleAdmin)
admin.site.register(Query, QueryAdmin)
# admin.site.register(Query) 