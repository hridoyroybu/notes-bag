# Generated by Django 4.2.4 on 2023-08-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]