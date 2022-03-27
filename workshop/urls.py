from django.urls import path
from workshop import views  
urlpatterns = [
    path('allworkshops/', views.allWorkshops),
    path('addworkshop/', views.addWorkshop),
    path('updateworkshop/', views.updateWorkshop),
    path('deleteworkshop/', views.deleteWorkshop),
    path('changeactive/', views.changeActive),
]