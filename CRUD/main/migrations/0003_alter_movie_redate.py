# Generated by Django 5.0.1 on 2024-02-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_movie_redate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='redate',
            field=models.DateField(),
        ),
    ]
