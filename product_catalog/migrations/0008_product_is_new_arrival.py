# Generated by Django 5.1 on 2024-10-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0007_alter_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new_arrival',
            field=models.BooleanField(default=False),
        ),
    ]
