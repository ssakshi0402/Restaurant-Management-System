# Generated by Django 3.2.6 on 2021-09-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_restro_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
