# Generated by Django 4.0.4 on 2022-05-22 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_info', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentinfo',
            old_name='seller',
            new_name='customer',
        ),
    ]
