# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_admin_conf_vars', '0002_auto_20150413_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurationvariable',
            name='editable',
            field=models.BooleanField(default=True),
        ),
    ]
