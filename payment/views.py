from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from .models import Ticket, TicketType, Order, ClubCard, Booking
from .serializers import TicketSerializer, \
    TicketTypeSerializer, \
    OrderSerializer, \
    ClubCardSerializer, \
    BookingSerializer, \
    TicketListSerializer, \
    OrderListSerializer, \
    BookingListSerializer, ClubCardListSerializer
from rest_framework.response import Response
from django.http import QueryDict
from rest_framework import serializers
from permissions.permissions import IsAdminAndIsOwnerOrReadOnly, AdminOrReadOnly
from .services import Pagination


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticated, IsAdminAndIsOwnerOrReadOnly, ]
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            tickets = Ticket.objects.all()
            page = self.paginate_queryset(tickets)
            if page is not None:
                serializer = TicketListSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = TicketListSerializer(tickets, many=True)
        else:
            tickets = Ticket.objects.filter(user=self.request.user)
            page = self.paginate_queryset(tickets)
            if page is not None:
                serializer = TicketListSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = TicketListSerializer(tickets, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        club_card = ClubCard.objects.get_or_create(user_id=self.request.user.id)
        data = QueryDict('', mutable=True)
        data['club_card'] = club_card[0].id
        data.update(request.data)
        serializer = TicketSerializer(data=data, context={'request': self.request})
        if serializer.is_valid():
            serializer.save(user=self.request.user, club_card_id=club_card[0].id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketTypeView(viewsets.ModelViewSet):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()
    permission_classes = [AdminOrReadOnly, ]


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, IsAdminAndIsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            serializer = OrderListSerializer(Order.objects.all(), many=True)
        else:
            serializer = OrderListSerializer(Order.objects.filter(user=self.request.user), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data, context={'request': self.request})
        tickets = Ticket.objects.filter(user_id=self.request.user.id, is_ordered=False)
        if len(tickets) == 0:
            raise serializers.ValidationError("You didn't pick tickets")
        if serializer.is_valid():
            serializer.save()
        tickets.update(order_id=serializer.instance.id, is_ordered=True)
        return Response(status=status.HTTP_201_CREATED)


class ClubCardView(viewsets.ModelViewSet):
    serializer_class = ClubCardSerializer
    queryset = ClubCard.objects.all()
    permission_classes = [IsAuthenticated, AdminOrReadOnly, ]
    http_method_names = ['get', ]

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            serializer = ClubCardListSerializer(ClubCard.objects.all(), many=True)
        else:
            serializer = ClubCardListSerializer(ClubCard.objects.filter(user=self.request.user), many=True)
        return Response(serializer.data)


class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated, IsAdminAndIsOwnerOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            serializer = BookingListSerializer(Booking.objects.all(), many=True)
        else:
            serializer = BookingListSerializer(Booking.objects.filter(user=self.request.user), many=True)
        return Response(serializer.data)
