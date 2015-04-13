from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from .global_vars import config


class ConfigurationVariableConfig(AppConfig):
    name = 'django_admin_conf_vars'
    verbose_name = _(u'Configuration variables')

    def ready(self):
        config.load_attributes()
