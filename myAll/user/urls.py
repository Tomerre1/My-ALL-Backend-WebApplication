
from django.urls import path,include
from user import views  
urlpatterns = [
    path('login/', views.userAuthentication),
    path('signup/', views.signUp),
]
