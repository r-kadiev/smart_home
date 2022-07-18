from django.urls import path

from smart_home import settings
from .views import SensorList, SensorView, MeasurementsList




urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsList.as_view()),
]