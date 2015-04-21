============================================
Django Administrable configuration variables
============================================

The django `django_admin_conf_vars` app allows you to have configuration variables for your project with the Django admin


# Installation
--------------

1. Install from `pip <https://pypi.python.org/pypi/django-admin-conf-vars>`_ ::

    $ pip install django-admin-conf-vars

2. Add `django_admin_conf_vars` to your INSTALLED_APPS

3. Migrate to create the databases::

        $ python manage.py migrate

Don't worry about the warnings, they are shown only the first time. (It's becouse the next configuration is not ready yet)

4. Create a python module named like you want. eg: 'my_var_settings_file.py' and put it into your project. eg: `my/path/package/my_var_settings_file.py`. Define your variables in that file::

    # -*- coding:utf-8 -*-
    from django_admin_conf_vars.global_vars import config

    config.set("MY_TIME_VAR", default=60)
    config.set("MY_OTHER_VAR", default="/some/path")
    ...

Be sure to have migrated and have the database created at this point. See `How to use <https://github.com/maoaiz/django-admin-conf-vars/wiki/How-to-use>`_


5. Add to your settings.py the path of your new module::
    
    VARS_MODULE_PATH = 'my_package.my_var_settings_file'


The variable VARS_MODULE_PATH must to have the name of your new file (point 4). Be sure to put it into an existing python package.


Ready! Now you have configuration variables with django admininistration.


## Upgrating from old version
-----------------------------

If You have installed previous versions, you need to migrate again, but first you must to comment the line in your settings.py `# VARS_MODULE_PATH = 'my_package.my_var_settings_file'`.

1. Comment the VARS_MODULE_PATH

2. Upgrade via pip `$ pip install --upgrade django_admin_conf_vars`.

3. Migrate `$ python manage.py migrate`

4. Uncomment the VARS_MODULE_PATH

5. Run the server



## Dependences
--------------

* Django >= 1.7


# How it works
--------------
`django_admin_conf_vars` use the Singleton design pattern to guarantee that only exists one instance of your configuration variables and that when you import the `config` variable always you have the global variables in a single object with your variables in its attributes. See `global_vars.py <https://github.com/MaoAiz/django-admin-conf-vars/blob/master/django_admin_conf_vars/global_vars.py>`_.


`django_admin_conf_vars` doesn't use the database every time you import it, it only connect to the database in two cases:


1. Every time you restart your server.

2. Every you modified a single var in the admin.


`django_admin_conf_vars` allows you to define global vars in your code, and too allows to edit them with the django admin. If you modify a variable with the admin, this always will keep the value of the database, and never will rewrite with the value inside the code. If you want to use the value inside the code, you can edit it in the admin and copy that value :)



# Differences between normal settings variables and django_admin_conf_vars
--------------------------------------------------------------------------

## Normal usage:
----------------
Your vars in the  settings.py::

    MY_TIME_VAR =  60
    MY_OTHER_VAR = "/some/path"


Using your vars in a view.py::

    from django.conf import settings

    def my_view(request):
        ...
        a = settings.MY_TIME_VAR
        b = settings.MY_OTHER_VAR
        ...


Conclusion: You have static variables written in your settings.py

but... what happen if you want to edit some of those variables in production? You need to edit the settings and reload your server. (Ͼ˳Ͽ)..!!!


## django_admin_conf_vars usage:
--------------------------------
You writte your variables and use them like normal usage.

Your vars in my_var_settings_file.py::

    # -*- coding:utf-8 -*-
    from django_admin_conf_vars.global_vars import config

    config.set("MY_TIME_VAR", default=60)
    config.set("MY_OTHER_VAR", default="/some/path")
    ...


And using your vars in a view.py::

    from django_admin_conf_vars.global_vars import config

    def my_view(request):
        ...
        a = config.MY_TIME_VAR
        b = config.MY_OTHER_VAR
        ...


Simple! Now you can edit those variables with the django admin



# Author & Contributors
-----------------------
* Created by `Mauricio Aizaga <https://github.com/maoaiz>`_. (`@maoaiz <https://twitter.com/maoaiz>`_ write me!)
* You

Feel free to send a `pull request <https://github.com/MaoAiz/django-admin-conf-vars/pulls>`_ to make a better software, I wait you.


