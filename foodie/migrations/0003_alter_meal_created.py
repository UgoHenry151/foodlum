# Generated by Django 4.0.2 on 2022-02-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0002_meal_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
