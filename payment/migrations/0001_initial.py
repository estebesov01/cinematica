# Generated by Django 4.0.4 on 2022-05-04 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ClubCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('payment', models.IntegerField(choices=[(1, 'Bank-card'), (2, 'Balance.kg'), (3, 'Элсом')])),
                ('is_ordered', models.BooleanField(default=False)),
                ('club_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.clubcard')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.order')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.seat')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.showtime')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.tickettype')),
            ],
        ),
    ]
