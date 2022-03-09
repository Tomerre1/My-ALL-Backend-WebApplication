
from django.urls import path
from step import views  
urlpatterns = [
    path('InsertStep/', views.InsertStep),
    path('updateStep/', views.updateStep),
    path('getAllSteps/', views.getAllSteps),
    path('deleteStep/', views.deleteStep),
    path('timeline/', views.getPath),
    path('next/', views.next),
    path('back/', views.back),
    path('delaysteps/', views.delaySteps),
]

