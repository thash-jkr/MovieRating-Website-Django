# Generated by Django 4.0.4 on 2022-07-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='fandango',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='metacritic',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rotten_tomatoes',
            field=models.FloatField(default=0),
        ),
    ]
