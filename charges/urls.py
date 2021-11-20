from django.urls   import path
from charges.views import DiscountView, PenaltyView

urlpatterns = [
    path("/discount", DiscountView.as_view()),
    path("/discount/<str:discount_id>", DiscountView.as_view()),
    path("/penalty", PenaltyView.as_view()),
    path("/penalty/<str:penalty_id>", PenaltyView.as_view()),
]
