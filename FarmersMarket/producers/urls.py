from django.urls import path
from FarmersMarket.producers import views

app_name = 'producers'
urlpatterns = [
    path('', views.ProducerListView.as_view(), name='list'),
    path('<int:pk>/', views.ProducerDetailView.as_view(), name='details'),
    path('add/', views.ProducerCreateView.as_view(), name='add'),
    path('<int:pk>/update/', views.ProducerUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProducerDeleteView.as_view(), name='delete'),
]