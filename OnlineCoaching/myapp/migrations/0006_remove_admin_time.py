# Generated by Django 3.2 on 2022-09-18 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_admin_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='time',
        ),
    ]
