# Generated by Django 4.2.4 on 2023-08-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_taskmodel_tasktitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filterId', models.IntegerField(default=1)),
            ],
        ),
    ]
