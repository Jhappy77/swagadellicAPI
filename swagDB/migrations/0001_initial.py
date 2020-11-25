# Generated by Django 3.1.3 on 2020-11-25 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField(verbose_name='release date')),
                ('length', models.IntegerField(default=90)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(verbose_name='birthday')),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screening_time', models.DateTimeField(verbose_name='start time')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swagDB.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theatre_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('seat_no', models.IntegerField()),
                ('screening_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swagDB.screening')),
                ('user_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='swagDB.registereduser')),
            ],
        ),
        migrations.AddField(
            model_name='screening',
            name='theatre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swagDB.theatre'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='swagDB.registereduser')),
            ],
        ),
    ]
