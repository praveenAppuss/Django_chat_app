# Generated by Django 5.0.1 on 2024-02-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('actor', models.CharField(max_length=25)),
                ('story', models.CharField(max_length=255)),
                ('redate', models.DateField()),
            ],
        ),
    ]
