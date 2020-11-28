# Generated by Django 3.1.3 on 2020-11-28 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swagDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Horror', 'Horror'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Drama', 'Drama'), ('Scifi', 'Scifi'), ('Nonfic', 'Non Fiction')], default='Action', max_length=20),
        ),
    ]