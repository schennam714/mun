# Generated by Django 2.2.3 on 2019-10-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191011_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='driver_form',
            field=models.FileField(default=None, null=True, upload_to='mcmunc_driver/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_ride',
            field=models.FileField(default=None, null=True, upload_to='mcmunc_rider/'),
        ),
    ]