
from django.urls import path
from level import views  
urlpatterns = [
    path('InsertLevel/', views.InsertLevel),
    path('updateLevel/', views.updateLevel),
    path('getAllLevels/', views.getAllLevels),
    path('deleteLevel/', views.deleteLevel),
    path('protocol/', views.protocol),
    
]

