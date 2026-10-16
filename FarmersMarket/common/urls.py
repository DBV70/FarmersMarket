from django.urls import path
from FarmersMarket.common import views

app_name = 'common'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]