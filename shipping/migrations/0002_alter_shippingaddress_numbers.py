# Generated by Django 3.2 on 2023-02-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='numbers',
            field=models.PositiveSmallIntegerField(),
        ),
    ]