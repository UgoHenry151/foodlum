# Generated by Django 4.0.2 on 2022-03-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0003_alter_shipping_admin_remark_alter_shipping_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='spice',
        ),
    ]