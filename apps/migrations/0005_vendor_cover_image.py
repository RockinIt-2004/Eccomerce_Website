# Generated by Django 5.0.3 on 2024-05-08 20:36

import apps.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_vendor_date_alter_product_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(default='vendor.jpg', upload_to=apps.models.user_directory_path),
        ),
    ]