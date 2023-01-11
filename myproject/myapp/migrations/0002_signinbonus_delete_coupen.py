# Generated by Django 4.1.5 on 2023-01-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupen_code', models.CharField(max_length=150)),
                ('coupen_max_usage', models.CharField(max_length=150)),
                ('coupen_discount', models.CharField(max_length=150)),
                ('maximum_discount', models.CharField(blank=True, max_length=150, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Coupen',
        ),
    ]
