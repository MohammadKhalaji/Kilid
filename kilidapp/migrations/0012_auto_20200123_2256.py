# Generated by Django 2.2.4 on 2020-01-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilidapp', '0011_houseimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_address',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]