# Generated by Django 3.2 on 2023-01-21 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0002_auto_20230109_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'charge'), (2, 'purchase'), (3, 'transfer received'), (4, 'transfer sent')], default=1),
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='received_transfers', to='transaction.transaction')),
                ('sender_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sent_transfers', to='transaction.transaction')),
            ],
        ),
    ]
