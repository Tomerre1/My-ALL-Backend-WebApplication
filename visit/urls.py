from django.urls import path
from visit import views  
urlpatterns = [
    path('allvisits/', views.allVisits),
    path('addvisit/', views.addVisit),
    path('updatevisit/', views.updateVisit),
    path('deletevisit/', views.deleteVisit),
    path('changeactive/', views.changeActive),
]