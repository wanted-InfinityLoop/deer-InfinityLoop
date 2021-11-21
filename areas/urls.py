from django.urls import path
from areas.views import ServiceAreaView, ServiceAreaDPView

urlpatterns = [
    path("/service/<str:charge_id>", ServiceAreaView.as_view()),
    path("/service", ServiceAreaDPView.as_view()),
]
