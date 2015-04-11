from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from .global_vars import config


class ConfVarConfig(AppConfig):
    name = 'django_admin_conf_vars'
    verbose_name = _(u'Global configuration variables')

    def ready(self):
        config.load_attributes()
