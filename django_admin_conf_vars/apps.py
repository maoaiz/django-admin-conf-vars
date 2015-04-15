from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ConfigurationVariableConfig(AppConfig):
    name = 'django_admin_conf_vars'
    verbose_name = _(u'Configuration variables')

    def ready(self):
        from .global_vars import config
        config.load_attributes()
