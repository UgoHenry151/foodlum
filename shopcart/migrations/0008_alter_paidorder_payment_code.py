# Generated by Django 4.0.2 on 2022-03-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0007_alter_paidorder_cart_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidorder',
            name='payment_code',
            field=models.CharField(max_length=100),
        ),
    ]
