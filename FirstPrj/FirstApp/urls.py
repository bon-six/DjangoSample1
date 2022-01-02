from django.urls import path
from .views import homepage_view
from .apps import FirstappConfig

app_name = FirstappConfig.name
urlpatterns = [
    path('', homepage_view, name='home'),
]