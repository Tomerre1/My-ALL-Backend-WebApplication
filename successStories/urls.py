from django.urls import path
from successStories import views  
urlpatterns = [
    path('allsuccessStories/', views.allSuccessStories),
    path('updatesuccessStory/', views.updateSuccessStory),
    path('deletesuccessStory/', views.deleteSuccessStory),
    path('addsuccessStory/', views.addSuccessStory),
]