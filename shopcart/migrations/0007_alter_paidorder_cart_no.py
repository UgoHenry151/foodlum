# Generated by Django 4.0.2 on 2022-03-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0006_shipping_paidorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidorder',
            name='cart_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]