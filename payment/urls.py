from django.urls import path, include
from movies.urls import router1
from . import views
from rest_framework.routers import DefaultRouter
router2 = DefaultRouter()
router2.register(r'ticket', views.TicketView)
router2.register(r'ticket_type', views.TicketTypeView)
router2.register(r'club_card', views.ClubCardView)
router2.register(r'booking', views.BookingView)
router2.register(r'order', views.OrderView)

urlpatterns = [
    path('', include(router2.urls))
]