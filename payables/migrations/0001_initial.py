# Generated by Django 4.0.4 on 2022-05-22 19:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('payment_date', models.DateField()),
                ('amount', models.FloatField()),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fees.fees')),
            ],
        ),
    ]
