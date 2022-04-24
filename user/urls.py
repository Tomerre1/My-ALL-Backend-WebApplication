
from django.urls import path,include
from user import views  
urlpatterns = [
    path('login/', views.userAuthentication),
    path('signup/', views.signUp),
    path('updateuser/', views.updateUser),
    path('getalluser/', views.getAllUsers),
    path('deleteuser/', views.deleteUser),

]
