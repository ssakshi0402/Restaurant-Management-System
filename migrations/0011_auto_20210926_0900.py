# Generated by Django 3.2.6 on 2021-09-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210910_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='zipcode',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
