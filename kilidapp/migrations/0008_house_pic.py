# Generated by Django 2.2.4 on 2020-01-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilidapp', '0007_remove_house_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pic',
            field=models.ImageField(default=None, upload_to='house_image'),
            preserve_default=False,
        ),
    ]
