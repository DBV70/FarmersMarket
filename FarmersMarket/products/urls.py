from django.urls import path
from FarmersMarket.products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='details'),
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
]
