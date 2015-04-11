from django.contrib import admin
from .models import ConfVar


class ConfVarAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_editable = ('value',)
    fields = ('name', 'value',)


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('name',) +  self.readonly_fields
        return self.readonly_fields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ConfVar, ConfVarAdmin)
