from django.utils import timezone

from rest_framework import serializers
from .models import Genre, Movie, MovieFormat, \
    Cinema, Room, RoomFormat, ShowTime, FeedBack, Seat


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_status(self, obj):
        now = timezone.now()
        if obj.start_release <= now <= obj.end_release:
            obj.status = 'current'
        elif obj.start_release > now:
            obj.status = 'upcoming'
        elif obj.end_release < now:
            obj.status = 'archive'
        return obj.status


class MovieListSerializer(MovieSerializer):
    genre = serializers.StringRelatedField()


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomListSerializer(RoomSerializer):
    cinema = serializers.StringRelatedField()
    format = serializers.StringRelatedField()


class RoomFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFormat
        fields = '__all__'


class ShowTimeSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = ShowTime
        fields = '__all__'

    def get_is_active(self, obj):
        if timezone.now() > obj.end:
            obj.is_active = False
        return obj.is_active


class ShowTimeListSerializer(ShowTimeSerializer):
    format = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()
    room = serializers.StringRelatedField()


class FeedBackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FeedBack
        fields = '__all__'


class FeedBackListSerializer(FeedBackSerializer):
    user = serializers.StringRelatedField()


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class SeatListSerializer(SeatSerializer):
    room = serializers.StringRelatedField()
