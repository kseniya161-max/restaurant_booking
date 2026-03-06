from django.urls import path

from booking.views import BookingPageView,ReservationCreateView,MyReservationListView,ReservationUpdateView,ReservationCancelView

app_name = "booking"

urlpatterns = [
    path('booking/', BookingPageView.as_view(), name='booking_list'),
    path('booking/add/', ReservationCreateView.as_view(), name='reservation_add'),
    path('booking/all/', MyReservationListView.as_view(), name='reservation_list'),
    path('booking/<int:pk>/edit/', ReservationUpdateView.as_view(), name='reservation_edit'),
    path('booking/<int:pk>/cancel/', ReservationCancelView.as_view(), name='reservation_cancel'),
    ]








