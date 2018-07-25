# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_admin_conf_vars', '0004_configurationvariable_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationvariable',
            name='description',
            field=models.TextField(default=True, help_text='The description can only be edited in the code.', blank=True),
        ),
        migrations.AlterField(
            model_name='configurationvariable',
            name='editable',
            field=models.BooleanField(default=True, help_text='The variable can be edited in the admin or not'),
        ),
    ]
