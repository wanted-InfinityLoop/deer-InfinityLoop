from django.urls    import path
from vehicles.views import LendKickboardView, ReturnKickboardView

urlpatterns = [
    path("/lend/<str:vehicle_id>",   LendKickboardView.as_view()),
    path("/return/<str:vehicle_id>", ReturnKickboardView.as_view())
]
