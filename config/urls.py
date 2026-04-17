from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("booking/", include("booking.urls")),
    path("users/", include("users.urls")),
    path("", include("pages.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

