from django.urls import path
from .views import TotalNetWorth, TopTenRichest, TopRichestWomen, WealthByGender


urlpatterns = [
    path('total_net_worth', TotalNetWorth, name='total_net_worth'),
    path('top_ten_richest', TopTenRichest, name='top_ten_richest'),
    path('top_richest_women', TopRichestWomen, name='top_richest_women'),
    path('wealth_by_gender', WealthByGender, name='wealth_by_gender'),
]
