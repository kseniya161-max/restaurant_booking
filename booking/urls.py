from django.urls import path

from booking.views import BookingPageView,ReservationCreateView,MyReservationListView,ReservationUpdateView,ReservationCancelView

app_name = "booking"

urlpatterns = [
    path('/', BookingPageView.as_view(), name='booking_list'),
    path('add/', ReservationCreateView.as_view(), name='reservation_add'),
    path('all/', MyReservationListView.as_view(), name='reservation_list'),
    path('<int:pk>/edit/', ReservationUpdateView.as_view(), name='reservation_edit'),
    path('<int:pk>/cancel/', ReservationCancelView.as_view(), name='reservation_cancel'),
    ]








