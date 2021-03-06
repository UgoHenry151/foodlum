# Generated by Django 4.0.2 on 2022-02-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0003_alter_meal_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'managed': True, 'verbose_name': 'Meal', 'verbose_name_plural': 'Meals'},
        ),
        migrations.AlterModelOptions(
            name='variety',
            options={'managed': True, 'verbose_name': 'Variety', 'verbose_name_plural': 'Varieties'},
        ),
        migrations.AddField(
            model_name='meal',
            name='menu',
            field=models.TextField(default='a'),
        ),
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(default='Medium', unique=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='variety',
            name='slug',
            field=models.SlugField(default='Medium', unique=True),
        ),
        migrations.AddField(
            model_name='variety',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, default='meal.jpg', null=True, upload_to='meal'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='spicy',
            field=models.CharField(choices=[('Not', 'Not'), ('Mild', 'Mild'), ('Medium', 'Medium'), ('Hot', 'Hot'), ('Extra Hot', 'Extra Hot')], default='Medium', max_length=100),
        ),
        migrations.AlterField(
            model_name='variety',
            name='image',
            field=models.ImageField(blank=True, default='variety.jpg', null=True, upload_to='variety'),
        ),
        migrations.AlterModelTable(
            name='meal',
            table='meal',
        ),
        migrations.AlterModelTable(
            name='variety',
            table='variety',
        ),
    ]
