# Generated by Django 2.2.3 on 2019-08-23 02:29

from django.db import migrations, models
import item.models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20190820_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=item.models.get_item_image_path),
        ),
    ]
