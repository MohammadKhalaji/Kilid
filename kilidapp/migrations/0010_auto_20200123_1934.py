# Generated by Django 2.2.4 on 2020-01-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilidapp', '0009_auto_20200123_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='bookmarked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='house',
            name='starred',
            field=models.BooleanField(default=False),
        ),
    ]
