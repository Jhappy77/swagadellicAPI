# Generated by Django 3.1.3 on 2020-11-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swagDB', '0002_auto_20201127_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_link',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]