from django.conf import settings
from .models import ConfVar
import os
import importlib
DEFAULT = 'global_vars'


class SingletonVar(object):

    ATTRIBUTES = {}

    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = super(SingletonVar, cls).__new__(cls, *a, **k)
        return cls._inst

    def __getattr__(self, key):
        if not bool(len(self.ATTRIBUTES)):
            self.load_attributes()
        return self.ATTRIBUTES.get(key, None)

    def getAll(self):
        if not bool(len(self.ATTRIBUTES)):
            self.load_attributes()
        return eval(str(self.ATTRIBUTES))

    def set(self, name, default=0):
        var, created = ConfVar.objects.get_or_create(name=name)
        if created:
            var.value = str(default)
            var.save(reload=False)
        self.ATTRIBUTES[var.name] = var.value

    def reload(self, name, value):
        self.ATTRIBUTES[name] = value

    def load_attributes(self):
        PROJECT_ROOT = os.environ['DJANGO_SETTINGS_MODULE'].split('.')[0]
        try:
            vars_path = settings.GLOBAL_VARS_PATH
        except Exception:
            vars_path = DEFAULT

        __import__(PROJECT_ROOT, fromlist=[vars_path])


config = SingletonVar()
