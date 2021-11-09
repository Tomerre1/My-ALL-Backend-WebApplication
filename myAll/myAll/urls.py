
from django.contrib import admin
from django.urls import path,include
from login import views as login_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
]
