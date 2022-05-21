# Generated by Django 4.0.4 on 2022-05-21 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('credit_fee', models.FloatField()),
                ('debit_fee', models.FloatField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
