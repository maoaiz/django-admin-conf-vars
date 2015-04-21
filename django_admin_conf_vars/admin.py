from django.contrib import admin
from .models import ConfigurationVariable


class ConfigurationVariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description', 'editable')
    fields = ('name', 'value', 'description', 'editable')
    list_editable = ('value',)
    class Media:
        css = {
             'all': ('django_admin_conf_vars/css/admin.css',)
        }
        js = [
            'django_admin_conf_vars/js/admin.js'
        ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            if not obj.editable:
                self.readonly_fields = ('value',)
            else:
                self.readonly_fields = ()
            return ('name', 'editable', 'description',) +  self.readonly_fields
        return self.readonly_fields


    def has_add_permission(self, request):
        return False


admin.site.register(ConfigurationVariable, ConfigurationVariableAdmin)
