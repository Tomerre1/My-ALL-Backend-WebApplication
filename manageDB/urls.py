
from django.urls import path
from manageDB import views  
urlpatterns = [
    path('createnewdb/', views.createNewDB),
    
    
]

