# Generated by Django 5.0.1 on 2024-02-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_movie_redate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='redate',
            field=models.DateField(auto_now=True),
        ),
    ]
