# Generated by Django 3.2 on 2022-09-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='name',
        ),
        migrations.AddField(
            model_name='admin',
            name='image',
            field=models.ImageField(default=False, upload_to='faculty_images/'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
