
from django.urls import path,include
from login import views as login_views
urlpatterns = [
    path('', login_views.userList),
    path('<int:pk>', login_views.userDetails),
]
