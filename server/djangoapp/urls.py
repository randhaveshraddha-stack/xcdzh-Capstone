from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path(route='', view=views.get_dealerships, name='index'),
    path(route='get_cars', view=views.get_cars, name='get_cars'),
    path(route='dealer/<int:dealer_id>/', view=views.get_dealer_details, name='dealer_details'),
    path(route='reviews/dealer/<int:dealer_id>/', view=views.get_dealer_reviews, name='dealer_reviews'),
    path(route='dealer/<int:dealer_id>/review', view=views.add_review, name='add_review'),
]
