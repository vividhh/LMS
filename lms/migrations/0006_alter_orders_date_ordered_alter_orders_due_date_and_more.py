# Generated by Django 4.1.1 on 2022-09-26 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_alter_orders_date_ordered_alter_orders_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date_ordered',
            field=models.DateField(default=datetime.datetime(2022, 9, 26, 3, 7, 18, 771788)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 1, 3, 7, 18, 771788)),
        ),
        migrations.AlterModelTable(
            name='books',
            table='Books',
        ),
    ]