from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dealerships, name='index'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),
]
