# Generated by Django 2.2.3 on 2019-10-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191012_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='next_conf',
            field=models.BooleanField(default=False),
        ),
    ]