from django.urls import path
from .views import my_index
from .views import my_gallery,my_about,my_booking


urlpatterns = [
  path('', my_index, name='my_index'),
  path('gallery/', my_gallery, name='my_gallery'),
  path('about/', my_about, name='my_about'),
    path('booking/', my_booking, name='my_booking'),

]
