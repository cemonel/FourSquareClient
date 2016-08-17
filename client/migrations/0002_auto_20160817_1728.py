# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searcher',
            old_name='food_name',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='searcher',
            old_name='location_name',
            new_name='location',
        ),
    ]
