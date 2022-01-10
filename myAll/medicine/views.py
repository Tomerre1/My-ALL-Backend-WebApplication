from .models import Medicine,MedicineForUser
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

@api_view(['POST'])
def getListMedicines(request):
    mail=request.data.get('mail')
    return Response(listMedicines(mail))





#------------------------------- help fucntions ----------------------------------#


def medicineForUser(mail,levelNumber):
    MedicineForUser.objects.filter(mail=mail).delete()
    medicineBylevel=list(filter(lambda m:levelNumber in m.levels,Medicine.objects.all()))
    for medicine in medicineBylevel:
        mfu=MedicineForUser(mail=mail,
                            medicineName=medicine.medicineName,
                            description=medicine.description,
                            count=medicine.count,
                            badInfluence=medicine.badInfluence,
                            foodOrNot=medicine.foodOrNot)
        mfu.days=[{'day':1, 'isActive':False},{'day':3, 'isActive':False},{'day':6, 'isActive':True}]
        mfu.save()


def listMedicines(mail):
    allmedicines=MedicineForUser.objects.filter(mail=mail)
    listMed=list([] for _ in range(1,8))
    for medicine in allmedicines:
        for day in medicine.days:
            tempMed={
                'day':day['day'],
                'medicineName':medicine.medicineName,
                'count':medicine.count,
                'isActive':day['isActive']
            }
            listMed[day['day']-1].append(tempMed)
    return listMed




       
        


