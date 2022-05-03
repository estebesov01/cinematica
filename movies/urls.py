from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router1 = DefaultRouter()
router1.register(r'genre', views.GenreView)
router1.register(r'movie', views.MovieView)
router1.register(r'movie_format', views.MovieFormatView)
router1.register(r'room', views.RoomView)
router1.register(r'room_format', views.RoomFormatView)
router1.register(r'cinema', views.CinemaView)
router1.register(r'feedback', views.FeedBackView)
router1.register(r'seat', views.SeatView)
router1.register(r'showtime', views.ShowTimeView)

urlpatterns = [
    path('', include(router1.urls))
]
