# Generated by Django 4.0.4 on 2022-11-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actor_description_director_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='url',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
