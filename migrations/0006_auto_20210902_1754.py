# Generated by Django 3.2.6 on 2021-09-02 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_restauranttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restauranttype',
            old_name='Restaurant_category',
            new_name='Restaurant_type',
        ),
        migrations.RenameField(
            model_name='restauranttype',
            old_name='Restaurant_image',
            new_name='Restauranttype_image',
        ),
    ]