# Generated by Django 5.0.3 on 2024-05-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_alter_productimages_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.ImageField(default='product.jpg', upload_to='product-images'),
        ),
    ]
