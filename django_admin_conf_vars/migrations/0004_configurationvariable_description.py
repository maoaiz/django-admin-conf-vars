# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_admin_conf_vars', '0003_configurationvariable_editable'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationvariable',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
