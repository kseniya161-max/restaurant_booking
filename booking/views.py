
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from booking.models import Table, Reservation
from booking.forms import ReservationForm


class BookingPageView(ListView):
    model = Table
    template_name = 'booking/booking.html'
    context_object_name = 'tables'


    def get_queryset(self):
        return Table.objects.filter(is_active=True)


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'booking/reservation_create.html'
    success_url = reverse_lazy('my_reservations')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Успешное бронирование')
        return super().form_valid(form)



class MyReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'booking/my_reservation.html'
    context_object_name = 'reservations'


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    fields = ["table", "date", "time", "guests"]
    template_name = 'booking/update_reservation.html'
    success_url = reverse_lazy('my_reservations')


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


    def form_valid(self,form):
        messages.success(self.request, 'Бронирование обновлено')
        return super().form_valid(form)



class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'booking/detail_reservation.html'
    context_object_name = 'reservation_detail'


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationCancelView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    fields = []
    success_url = reverse_lazy('my_reservations')


    def form_valid(self, form):
        form.instance.status = 'cancelled'
        messages.success(self.request, "Бронирование отменено")
        return super().form_valid(form)

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)














