# Generated by Django 2.2.4 on 2020-01-23 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kilidapp', '0006_auto_20200123_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='pic',
        ),
    ]