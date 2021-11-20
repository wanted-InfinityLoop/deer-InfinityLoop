from django.urls   import path
from charges.views import DiscountView


urlpatterns = [
    path("/discount", DiscountView.as_view()),
]
