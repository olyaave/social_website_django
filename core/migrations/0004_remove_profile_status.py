# Generated by Django 4.1.3 on 2022-12-22 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_subscribes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
    ]
