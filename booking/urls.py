from django.urls import path

from booking.views import (
    BookingPageView,
    MyReservationListView,
    ReservationUpdateView,
    ReservationCancelView,
    ReservationDetailView,
)

app_name = "booking"

urlpatterns = [
    path("", BookingPageView.as_view(), name="booking"),
    # path('add/', ReservationCreateView.as_view(), name='reservation_add'),
    path("all/", MyReservationListView.as_view(), name="my_reservations"),
    path("<int:pk>/", ReservationDetailView.as_view(), name="reservation_detail"),
    path("<int:pk>/edit/", ReservationUpdateView.as_view(), name="reservation_edit"),
    path(
        "<int:pk>/cancel/", ReservationCancelView.as_view(), name="reservation_cancel"
    ),
]
