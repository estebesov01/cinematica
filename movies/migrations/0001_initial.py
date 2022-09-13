# Generated by Django 4.0.4 on 2022-05-04 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('contacts', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True)),
                ('rate', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age_limit', models.PositiveSmallIntegerField()),
                ('start_release', models.DateTimeField()),
                ('end_release', models.DateTimeField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('content', models.TextField(blank=True)),
                ('country', models.CharField(max_length=128)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='RoomFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movieformat')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.room')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_seat', models.SmallIntegerField()),
                ('num_row', models.SmallIntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.roomformat'),
        ),
    ]
