from django.urls import path
from vehicles    import views

urlpatterns = [
    path("/lend", views.LendKickboardView.as_view()),
]
