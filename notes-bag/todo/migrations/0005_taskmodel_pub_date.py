# Generated by Django 4.2.4 on 2023-08-15 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_taskmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 8, 15, 5, 46, 41, 320852, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
