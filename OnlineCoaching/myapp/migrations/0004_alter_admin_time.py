# Generated by Django 3.2 on 2022-09-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220919_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='time',
            field=models.DateField(),
        ),
    ]
