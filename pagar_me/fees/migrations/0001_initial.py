# Generated by Django 4.0.4 on 2022-05-22 19:14
from datetime import datetime
from django.db import migrations, models
from django.db.migrations.state import StateApps
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from uuid import uuid4


def insert_initial_fees(apps: StateApps, schema_editor: DatabaseSchemaEditor):
    fees = apps.get_model('fees', 'Fees')

    fee = {
        'id': uuid4(),
        'credit_fee': '0.05',
        'debit_fee': '0.03',
        'created_at': datetime.now(),
    }

    fees.objects.create(**fee)

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
