# Generated by Django 4.2.1 on 2024-06-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_cart_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_product',
            name='user',
            field=models.CharField(default='vamsi', max_length=150),
        ),
    ]
