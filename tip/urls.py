from django.urls import path
from tip import views  
urlpatterns = [
    path('alltips/', views.allTips),
    path('updatetip/', views.updateTip),
    path('deletetip/', views.deleteTip),
    path('addtip/', views.addTip),
]