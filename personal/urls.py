from django.urls import path
from . import views


app_name = "personals"

urlpatterns = [
    path('', views.home_screen_view, name="home_screen_view")
]