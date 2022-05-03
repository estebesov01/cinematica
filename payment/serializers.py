from rest_framework import serializers
from .models import Ticket, ClubCard, Booking, Order, TicketType


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['price', 'club_card', 'is_ordered', 'order']

    def validate(self, data):
        seat = data.get('seat')
        show_time = data.get('show_time')
        if Booking.objects.filter(seat=seat, show_time=show_time, user=data.get('user')).exists():
            return data
        if Booking.objects.filter(seat=seat, show_time=show_time).exists():
            raise serializers.ValidationError('This seat is already reserved.')
        elif Ticket.objects.filter(seat=seat, show_time=show_time).exists():
            raise serializers.ValidationError('This seat already bought')
        return data


class TicketListSerializer(TicketSerializer):
    payment = serializers.SerializerMethodField()
    user = serializers.StringRelatedField()
    ticket_type = serializers.StringRelatedField()
    seat = serializers.StringRelatedField()
    show_time = serializers.StringRelatedField()
    club_card = serializers.StringRelatedField()

    def get_payment(self, obj):
        choice = Ticket.objects.get(id=obj.id)
        for i in Ticket.methods:
            if choice.payment == i[0]:
                return i[1]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_price(self, obj):
        tickets = Ticket.objects.filter(order=obj.id, is_ordered=True)
        total_price = 0
        for ticket in tickets:
            total_price += ticket.price
        return total_price


class OrderListSerializer(OrderSerializer):
    user = serializers.StringRelatedField()
    tickets = TicketListSerializer(many=True, source='ticket_set')


class ClubCardSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    balance = serializers.SerializerMethodField()

    class Meta:
        model = ClubCard
        fields = '__all__'

    def get_balance(self, obj):
        orders = Ticket.objects.filter(user=obj.user, is_ordered=True)
        balance = 0
        for i in orders:
            print(i.price)
            balance += i.price * 0.03
        return balance


class ClubCardListSerializer(ClubCardSerializer):
    user = serializers.StringRelatedField()


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        seat = data.get('seat')
        show_time = data.get('show_time')
        if Booking.objects.filter(seat=seat, show_time=show_time).exists():
            raise serializers.ValidationError('This seat is already reserved.')
        elif Ticket.objects.filter(seat=seat, show_time=show_time).exists():
            raise serializers.ValidationError('This seat already bought')
        return data


class BookingListSerializer(BookingSerializer):
    user = serializers.StringRelatedField()
    seat = serializers.StringRelatedField()
    show_time = serializers.StringRelatedField()
