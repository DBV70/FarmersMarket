from django.urls import path
from FarmersMarket.markets import views

app_name = 'markets'
urlpatterns = [
    path('', views.MarketListView.as_view(), name='list'),
    path('<int:pk>/', views.MarketDetailView.as_view(), name='details'),
    path('add/', views.MarketCreateView.as_view(), name='add'),
    path('<int:pk>/update/', views.MarketUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.MarketDeleteView.as_view(), name='delete'),
]