# Generated by Django 3.2.6 on 2021-09-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_customer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
