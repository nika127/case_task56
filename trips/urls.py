from django.urls import path
from . import views
from .views import trip_create, trip_list, trip_detail 


urlpatterns = [
    path('create/', trip_create, name='trip_create'),
    path('', trip_list, name='trip_list'),  # URL для списка путешествий
    path('<int:trip_id>/', trip_detail, name='trip_detail'),
]
