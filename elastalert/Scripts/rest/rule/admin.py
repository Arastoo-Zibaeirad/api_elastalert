from django.contrib import admin
from .models import Rule, Query, Config

# Register your models here.

class QueryInline(admin.TabularInline):
    model = Query
    extra = 1

class ConfigInline(admin.TabularInline):
    model = Config

class RuleAdmin(admin.ModelAdmin):
    # class Meta:
    #     model = Rule
    list_display = ['id', 'name', 'index_name','sequence', 'create_time', 'modified_time','total']
    search_fields = ['name', 'index_name', 'create_time', 'modified_time']
    list_display_links = ['name']
    inlines = [
        QueryInline,
        ConfigInline,
        ]
    
    # def qt(self, request):
    #     rule = Rule.objects.all()
    #     # q = rule.queries.all()
    #     return q

class QueryAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_category', 'condition',]
    # list_editable = ['sequence']
    search_field = ['event_category', 'condition']


admin.site.register(Rule, RuleAdmin)
admin.site.register(Query, QueryAdmin)
# admin.site.register(Query) 