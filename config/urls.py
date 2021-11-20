from django.urls import path, include

urlpatterns = [
    path("users", include("users.urls")),
    path("vehicles", include("vehicles.urls")),
    path("charges", include("charges.urls")),
]
