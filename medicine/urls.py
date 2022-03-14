
from django.urls import path
from medicine import views  
urlpatterns = [
    path('addmedicine/', views.addMedicine),
    path('updatemedicine/', views.updateMedicine),
    path('deleteMedicine/', views.deleteMedicine),
    path('allmedicines/', views.allMedicines),
    path('getListMedicines/', views.getListMedicines),
    path('addMedicineForDay/', views.addMedicineForDay),
    path('removeMedicineFromDay/', views.removeMedicineFromDay),
    path('changeActive/', views.changeActive),
    path('restartMedicineList/', views.restartMedicineList),
    path('getListMedicineNames/', views.getListMedicineNames),
]
