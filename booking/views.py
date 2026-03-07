from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from booking.models import Table, Reservation
from booking.forms import ReservationForm
from django.core.mail import send_mail
from django.conf import settings


class BookingPageView(ListView):
    model = Table
    template_name = 'booking.html'
    context_object_name = 'tables'


    def get_queryset(self):
        return Table.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)

            reservation.user = request.user
            reservation.status = 'confirmed'

            reservation.save()

            send_mail(
                subject='Бронирование подтверждено',
                message=f'Ваше бронирование подтверждено. Стол: {reservation.table} '
                        f'Дата: {reservation.date} Время: {reservation.time}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=True
            )

            messages.success(request, "Бронирование успешно создано")

            return redirect('booking:reservation_detail', pk=reservation.pk)

        context = self.get_context_data()
        context['form'] = form

        return render(request, self.template_name, context)




# class ReservationCreateView(LoginRequiredMixin, CreateView):
#     model = Reservation
#     form_class = ReservationForm
#     template_name = 'booking/reservation_create.html'
#     success_url = reverse_lazy('my_reservations')
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.status = 'confirmed'
#         response = super().form_valid(form)
#
#         send_mail(
#             subject='Бронирование подтверждено',
#             message=f'Ваше бронирование подтверждено.Стол: {self.object.table} Дата: {self.object.date} Время: {self.object.time} Гостей: {self.object.guests}',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[self.request.user.email],
#             fail_silently=True
#         )
#         messages.success(self.request, 'Бронирование успешно создано')
#         return response
#






class MyReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'booking/my_reservation.html'
    context_object_name = 'reservations'


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'booking/update_reservation.html'
    success_url = reverse_lazy('booking:reservation_list')


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


    def form_valid(self,form):
        messages.success(self.request, 'Бронирование обновлено')
        return super().form_valid(form)



class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'booking/detail_reservation.html'
    context_object_name = 'reservation'


    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class ReservationCancelView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('my_reservations')


    def form_valid(self, form):
        form.instance.status = 'cancelled'
        messages.success(self.request, "Бронирование отменено")
        return super().form_valid(form)

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)














