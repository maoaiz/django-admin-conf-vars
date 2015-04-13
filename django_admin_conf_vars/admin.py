from django.contrib import admin
from .models import ConfigurationVariable


class ConfigurationVariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_editable = ('value',)
    fields = ('name', 'value',)


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('name',) +  self.readonly_fields
        return self.readonly_fields

    def has_add_permission(self, request):
        return False


admin.site.register(ConfigurationVariable, ConfigurationVariableAdmin)
