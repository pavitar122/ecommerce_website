# Generated by Django 4.2.3 on 2024-02-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0005_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='pin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.TextField(),
        ),
    ]