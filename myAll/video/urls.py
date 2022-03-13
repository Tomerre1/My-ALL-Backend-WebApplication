from django.urls import path
from video import views  
urlpatterns = [
    path('addvideo/', views.addVideo),
    path('updatevideo/', views.updateVideo),
    path('deletevideo/', views.deleteVideo),
    path('allvideos/', views.allVideos),
]