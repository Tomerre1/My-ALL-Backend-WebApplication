
from django.urls import path
from step import views  
urlpatterns = [
    path('timeline/', views.getPath),
]

