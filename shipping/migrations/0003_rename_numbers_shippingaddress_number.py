# Generated by Django 3.2 on 2023-02-02 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_alter_shippingaddress_numbers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='numbers',
            new_name='number',
        ),
    ]
