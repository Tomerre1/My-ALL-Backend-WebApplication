from django.urls import path
from contact import views  
urlpatterns = [
    path('addcontact/', views.addContact),
    path('updatecontact/', views.updateContact),
    path('deletecontact/', views.deleteContact),
    path('allcontacts/', views.allContacts),
]