from .models import Medicine
from .serializers import MedicineSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def allMedicines(request):
    medicines = Medicine.objects.all()
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addMedicine(request):
    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateMedicine(request):
    medicine = Medicine.objects.get(
        medicineName=(request.data.get('medicineName')))
    serializer = MedicineSerializer(medicine, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteMedicine(request):
    try:
        medicine = Medicine.objects.get( medicineName=(request.data.get('medicineName')))
    except Medicine.DoesNotExist:
        return Response({'message': 'ERROR'})
    medicine.delete()
    return Response({'message': 'deleted successfuly'})
