from .models import Medicine
from .serializers import MedicineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#token=5cbce175d45037d379e125dd7a65104063e8b7a5

@api_view(['GET'])
def allMedicines(request):
    return getAllMedicines(request)

@api_view(['POST',])
def addMedicine(request):
    serializer=MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return getAllMedicines(request)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateMedicine(request):
    medicine=Medicine.objects.get(medicineName=(request.data.get('medicineName')))
    serializer=MedicineSerializer(medicine,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return getAllMedicines(request)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteMedicine(request):
    medicine=Medicine.objects.get(medicineName=(request.data.get('medicineName')))
    medicine.delete()
    return getAllMedicines(request)

########################### Help functions ##########################

def getAllMedicines(request):
    medicines=Medicine.objects.all()
    serializer= MedicineSerializer(medicines ,many=True)
    return Response(serializer.data)

    