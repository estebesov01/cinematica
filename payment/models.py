from django.db import models
from user.models import CustomUser
from movies.models import ShowTime, Seat


class TicketType(models.Model):
    name = models.CharField(max_length=128)
    price = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.user.email


class ClubCard(models.Model):
    balance = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Ticket(models.Model):
    methods = [
        (1, 'Bank-card'),
        (2, 'Balance.kg'),
        (3, 'Элсом'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    price = models.IntegerField()
    payment = models.IntegerField(choices=methods)
    club_card = models.ForeignKey(ClubCard, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    is_ordered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.price = self.ticket_type.price + self.show_time.format.price + self.seat.room.format.price
        super().save(*args, **kwargs)


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
