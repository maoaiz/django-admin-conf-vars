# Django Administrable configuration varialbes
The django `django_admin_conf_vars` app allows you to have configuration variables for your project with the Django admin


### Installation

1. Install from [pypi](https://pypi.python.org/pypi/django-admin-conf-vars): `pip install django-admin-conf-vars`

2. Add `django_admin_conf_vars` to your INSTALLED_APPS

3. Migrate `python manage.py migrate`

4. Create a file 'my_settings_conf.py' next to your settings.py and define your variables
    ```python
    from django_admin_conf_vars.global_vars import config
    config.set("MY_TIME_VAR", default=60)
    config.set("MY_OTHER_VAR", default="/some/path")
    ```

5. Add to your settings.py file:
    ```python
    GLOBAL_VARS_PATH = 'my_package.my_settings_conf'
    ```
The variable GLOBAL_VARS_PATH must to have the name of your new file (point 4). Be sure to locale in a python package.

Ready! Now you have configuration variables with [django admininistration](http://localhost:8000/admin/django_admin_conf_vars/confvar/).



### Dependences
* Django >= 1.7

### Differences between normal settings variables and django_admin_conf_vars
----

#### Normal:
Your vars in the  settings.py

```python
MY_TIME_VAR =  60
MY_OTHER_VAR = "/some/path"
```

Using your vars in a view.py
```python
from django.conf import settings

def my_view(request):
    ...
    a = settings.MY_TIME_VAR
    b = settings.MY_OTHER_VAR
```

Conclusion: You have static variables written in your settings.py

but... what happen if you want to edit some of those variables in production? You need to edit the settings and reload your server. (Ͼ˳Ͽ)..!!!

#### With django_admin_conf_vars
You writte your variables and use them like normal usage.

Your vars in my_var_settings_file.py

```python
from django_admin_conf_vars.global_vars import config

config.set("MY_TIME_VAR", default=60)
config.set("MY_OTHER_VAR", default="/some/path")
```

And using your vars in a view.py
```python
from django_admin_conf_vars.global_vars import config

def my_view(request):
    ...
    a = config.MY_TIME_VAR
    b = config.MY_OTHER_VAR
```

Now you can edit those variables with the [django admin](http://localhost:8000/admin/django_admin_conf_vars/confvar/):




### How it works
django_admin_conf_vars use the Singleton design pattern to guaranteeing that only exist one instance of your configuration variables and your view calls doesn't use the database every time, but rather a single object with your variables as attributes. See [global_vars.py](https://github.com/MaoAiz/django-admin-conf-vars/blob/master/django_admin_conf_vars/global_vars.py#L12)



### Author
Created by [Mauricio Aizaga](https://github.com/maoaiz)
