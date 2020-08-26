from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('index2', views.index2, name="index2"),
    path('index3', views.index3, name="index3"),
    path('index4', views.index4, name="index4"),
    path('predict', views.predict, name="predict"),
    path('about/', views.about, name="about"),
]
