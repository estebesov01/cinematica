from rest_framework import viewsets, status
from .models import Genre, Movie, MovieFormat, RoomFormat, Room, ShowTime, Cinema, FeedBack, Seat
from .serializers import GenreSerializer, MovieSerializer, MovieFormatSerializer, RoomFormatSerializer, \
    CinemaSerializer, SeatSerializer, FeedBackSerializer, FeedBackListSerializer, RoomSerializer, RoomListSerializer, \
    SeatListSerializer, ShowTimeSerializer, ShowTimeListSerializer, MovieListSerializer
from django.utils import timezone
from permissions.permissions import AdminOrReadOnly, IsAdminAndIsOwnerOrReadOnly
from rest_framework.response import Response


class GenreView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [AdminOrReadOnly, ]


class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(end_release__gt=timezone.now())
    permission_classes = [AdminOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        serializer = MovieListSerializer(Movie.objects.all(), many=True)
        return Response(serializer.data)


class MovieFormatView(viewsets.ModelViewSet):
    serializer_class = MovieFormatSerializer
    queryset = MovieFormat.objects.all()
    permission_classes = [AdminOrReadOnly, ]


class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [AdminOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        serializer = RoomListSerializer(Room.objects.all(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            seats = serializer.data['amount_of_seat']
            rows = serializer.data['amount_of_row']
            room_id = serializer.data['id']
            print(seats, rows, room_id)
            for i in range(1, seats + 1):
                for j in range(1, rows + 1):
                    Seat.objects.create(num_seat=i, num_row=j, room_id=room_id)
        return Response(status=status.HTTP_201_CREATED)


class RoomFormatView(viewsets.ModelViewSet):
    serializer_class = RoomFormatSerializer
    queryset = RoomFormat.objects.all()
    permission_classes = [AdminOrReadOnly, ]


class CinemaView(viewsets.ModelViewSet):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    permission_classes = [AdminOrReadOnly, ]


class FeedBackView(viewsets.ModelViewSet):
    serializer_class = FeedBackSerializer
    queryset = FeedBack.objects.all()
    permission_classes = [IsAdminAndIsOwnerOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        serializer = FeedBackListSerializer(FeedBack.objects.all(), many=True)
        return Response(serializer.data)


class SeatView(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
    permission_classes = [AdminOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        serializer = SeatListSerializer(Seat.objects.all(), many=True)
        return Response(serializer.data)


class ShowTimeView(viewsets.ModelViewSet):
    serializer_class = ShowTimeSerializer
    queryset = ShowTime.objects.all()
    permission_classes = [AdminOrReadOnly, ]

    def list(self, request, *args, **kwargs):
        serializer = ShowTimeListSerializer(ShowTime.objects.all(), many=True)
        return Response(serializer.data)
