
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='booking/')),
    path('booking/', include('booking.urls')),
    path('users/', include('users.urls')),
    path('pages/', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
