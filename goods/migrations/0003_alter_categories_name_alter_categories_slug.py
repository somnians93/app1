# Generated by Django 4.2.7 on 2024-05-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
    ]
