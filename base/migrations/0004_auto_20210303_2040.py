# Generated by Django 3.1.6 on 2021-03-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shippingPrice',
        ),
        migrations.RemoveField(
            model_name='order',
            name='taxPrice',
        ),
    ]
