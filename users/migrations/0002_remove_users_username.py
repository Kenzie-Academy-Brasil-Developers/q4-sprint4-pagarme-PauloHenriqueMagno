# Generated by Django 4.0.4 on 2022-05-22 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
    ]
