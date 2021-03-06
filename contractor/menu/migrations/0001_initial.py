# Generated by Django 3.0.2 on 2020-03-06 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True, verbose_name='menu name')),
                ('slug', models.SlugField(max_length=24, unique=True)),
                ('additional_text', models.CharField(blank=True, max_length=128, null=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the item on the menu.', max_length=48)),
                ('description', models.CharField(blank=True, help_text='Description of a menu item.', max_length=128, null=True)),
                ('price', models.IntegerField(help_text='The price in the cost of the item.')),
                ('classification', models.CharField(choices=[('neither', 'Neither'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian')], default=0, help_text='Select if this item classifies as Vegetarian, Vegan, or Neither.', max_length=10, verbose_name='classification')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
            },
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='menu category name')),
                ('additional_text', models.CharField(blank=True, max_length=128, null=True)),
                ('order', models.IntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Menu')),
            ],
            options={
                'verbose_name': 'menu category',
                'verbose_name_plural': 'menu catagories',
                'ordering': ['name', 'order'],
            },
        ),
    ]
