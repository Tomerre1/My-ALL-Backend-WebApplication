
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('medicine/',include('medicine.urls')),
    path('step/',include('step.urls')),
    path('level/',include('level.urls')),
    path('video/',include('video.urls')),
    path('contact/',include('contact.urls')),
    path('tip/',include('tip.urls')),
    path('successStories/',include('successStories.urls')),
]
