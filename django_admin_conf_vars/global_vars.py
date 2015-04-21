from django.conf import settings
from .models import ConfigurationVariable
import os
import importlib
VARS_MODULE_PATH_DEFAULT = 'global_vars'


class VariablesManager(object):

    ATTRIBUTES = {}

    def __new__(cls, *a, **k):
        '''Constructor to make a Singleton class'''
        if not hasattr(cls, '_inst'):
            cls._inst = super(VariablesManager, cls).__new__(cls, *a, **k)
        return cls._inst

    def __getattr__(self, key):
        '''Give access to the values of the ATTRIBUTES dictionary
        eg: config.ATTRIBUTES['MY_VAR'] is equal to config.MY_VAR'''
        if not bool(len(self.ATTRIBUTES)):
            self.load_attributes()
        return self.ATTRIBUTES.get(key, None)

    def getAll(self):
        '''Return a dictionary with all variables'''
        if not bool(len(self.ATTRIBUTES)):
            self.load_attributes()
        return eval(str(self.ATTRIBUTES))

    def set(self, name, default=0, editable=True, description=""):
        '''Define a variable in DB and in memory'''
        var, created = ConfigurationVariable.objects.get_or_create(name=name)
        if created:
            var.value = default
        if not editable:
            var.value = default
        var.editable = editable
        var.description = description
        var.save(reload=False)
        self.ATTRIBUTES[var.name] = var.value  # ATTRIBUTES is accesible by any instance of VariablesManager

    def reload(self, name, value):
        '''Update a variable in memory. ConfigurationVariable model use this method when a variable is
        updated via de django admin'''
        self.ATTRIBUTES[name] = value

    def load_attributes(self):
        '''Read the variables from the VARS_MODULE_PATH'''
        try:
            vars_path = settings.VARS_MODULE_PATH
        except Exception:
            print "*******************************************************"
            print "[WARNING] No VARS_MODULE_PATH defined in your settings,\nUsing default module '{}'. \n".format(VARS_MODULE_PATH_DEFAULT)
            vars_path = VARS_MODULE_PATH_DEFAULT

        try:
            __import__(vars_path)
        except ImportError:
            print "*******************************************************"
            print "[WARNING] No module named '{}'. \n\nPlease, read the documentation https://github.com/MaoAiz/django-admin-conf-vars#installation\n".format(vars_path)



config = VariablesManager()
