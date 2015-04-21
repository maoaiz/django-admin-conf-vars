from django.db import models
from django.utils.translation import ugettext_lazy as _


class ConfigurationVariable(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    editable = models.BooleanField(default=True,
        help_text=_(u'The variable can be edited in the admin or not'))
    description = models.TextField(default=True,
        blank=True,
        help_text=_(u'The description can only be edited in the code.'))
    
    def save(self, reload=True, *args, **kwargs):
        res = super(ConfigurationVariable, self).save(*args, **kwargs)
        if reload:
            from .global_vars import config
            config.reload(self.name, self.value)
        return res 

    def get_absolute_url(self):
        return self.name

    def __unicode__(self):
        return u"%s: %s" %(self.name, self.value)

    class Meta:
        verbose_name = _(u'Variable')
        verbose_name_plural = _(u'Variables list')