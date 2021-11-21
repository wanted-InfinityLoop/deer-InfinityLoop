from django.urls import path
from areas.views import ServiceAreaView

urlpatterns = [
    path("/service/<str:charge_id>", ServiceAreaView.as_view()),
]
