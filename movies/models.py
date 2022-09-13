from django.db import models

from user.models import CustomUser


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=128)
    age_limit = models.PositiveSmallIntegerField()
    start_release = models.DateTimeField()
    end_release = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    country = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MovieFormat(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=128)
    start = models.TimeField(auto_now_add=False)
    end = models.TimeField(auto_now_add=False)
    location = models.CharField(max_length=200)
    contacts = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class RoomFormat(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=128)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    format = models.ForeignKey(RoomFormat, on_delete=models.CASCADE)
    amount_of_seat = models.PositiveSmallIntegerField(default=15)
    amount_of_row = models.PositiveSmallIntegerField(default=8)

    def __str__(self):
        return self.name




class ShowTime(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    format = models.ForeignKey(MovieFormat, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.movie.name} {self.start}'


class FeedBack(models.Model):
    rates = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    rate = models.IntegerField(choices=rates)

    def __str__(self):
        return self.title


class Seat(models.Model):
    num_seat = models.SmallIntegerField()
    num_row = models.SmallIntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'row - {self.num_row} seat - {self.num_seat}'
