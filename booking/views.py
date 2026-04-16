from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from booking.models import Table, Reservation
from booking.forms import ReservationForm
from django.conf import settings


class BookingPageView(LoginRequiredMixin, ListView):
    model = Table
    template_name = "booking.html"
    context_object_name = "tables"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)

            reservation.user = request.user
            reservation.status = "confirmed"

            reservation.save()

            request.user.email_user(
                subject="Бронирование подтверждено",
                message=(
                    f"Ваше бронирование подтверждено.\n"
                    f"Стол: {reservation.table}\n"
                    f"Дата: {reservation.date}\n"
                    f"Время: {reservation.time}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
            )

            messages.success(request, "Бронирование успешно создано")

            return redirect("booking:reservation_detail", pk=reservation.pk)

        context = self.get_context_data(object_list=self.get_queryset())
        context["form"] = form
        return render(request, self.template_name, context)


class MyReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "my_reservation.html"
    context_object_name = "reservations"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "update_reservation.html"
    success_url = reverse_lazy("booking:my_reservations")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Бронирование обновлено")
        return super().form_valid(form)


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = "detail_reservation.html"
    context_object_name = "reservation"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ReservationCancelView(LoginRequiredMixin, UpdateView):
    model = Reservation
    fields = []
    template_name = "reservation_cancel.html"
    success_url = reverse_lazy("booking:my_reservations")

    def form_valid(self, form):
        form.instance.status = "cancelled"
        messages.success(self.request, "Бронирование отменено")
        return super().form_valid(form)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
