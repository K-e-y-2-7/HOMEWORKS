# Generated by Django 3.2.9 on 2021-11-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_year_of_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_public',
            field=models.DateField(default='2021-01-01'),
        ),
    ]