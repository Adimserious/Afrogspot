# Generated by Django 5.1 on 2024-10-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0006_productrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
