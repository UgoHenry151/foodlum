# Generated by Django 4.0.2 on 2022-02-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0020_meal_max_order_meal_min_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='paidorder',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='PaidOrder',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
        migrations.DeleteModel(
            name='Shopcart',
        ),
    ]
