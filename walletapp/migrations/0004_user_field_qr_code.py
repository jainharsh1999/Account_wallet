# Generated by Django 4.1.3 on 2022-12-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0003_delete_wallet_payment_user_field_add_money_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_field',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_code'),
        ),
    ]