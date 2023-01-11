# Generated by Django 4.1.5 on 2023-01-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_signinbonus_delete_coupen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signinbonus',
            old_name='coupen_code',
            new_name='limit_voucher_usage',
        ),
        migrations.RenameField(
            model_name='signinbonus',
            old_name='coupen_discount',
            new_name='voucher_code',
        ),
        migrations.RenameField(
            model_name='signinbonus',
            old_name='message',
            new_name='voucher_description',
        ),
        migrations.RenameField(
            model_name='signinbonus',
            old_name='coupen_max_usage',
            new_name='voucher_discount',
        ),
        migrations.AddField(
            model_name='signinbonus',
            name='voucher_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]