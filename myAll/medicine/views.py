from .models import Medicine,MedicineForUser
from .serializers import MedicineSerializer,MedicineForUserSerializer
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


@api_view(['POST'])
def removeMedicineFromDay(request):
    mail=request.data.get('mail')
    medicineName=request.data.get("medicineName")
    day=str(indexDay(request.data.get('day')))
    mfu= MedicineForUser.objects.get(mail=mail,medicineName=medicineName)
    mfu.days.pop(day)
    mfu.save()
    if not mfu.days:
        mfu.delete()
    return Response("")




@api_view(['POST'])
def addMedicineForDay(request):
    mail=request.data.get('mail')
    medicineName=request.data.get("medicineName")
    count=request.data.get('count')
    day=str(indexDay(request.data.get('day')))
    try:
        mfu= MedicineForUser.objects.get(mail=mail,medicineName=medicineName)
        mfu.count=count
        mfu.days[day]=False
        mfu.save()
    except MedicineForUser.DoesNotExist:
        mfu=MedicineForUser(mail=mail,medicineName=medicineName,count=count)            
        mfu.days[day]=False
        mfu.save()
    return Response(MedicineForUserSerializer(mfu).data)


@api_view(['POST'])
def changeActive(request):
    mail=request.data.get('mail')
    medicineName=request.data.get("medicineName")
    day=str(indexDay(request.data.get('day')))
    mfu= MedicineForUser.objects.get(mail=mail,medicineName=medicineName)
    mfu.days[day]=not(mfu.days[day])
    mfu.save()
    return Response(MedicineForUserSerializer(mfu).data)    

@api_view(['POST']) 
def restartMedicineList(request):
    mail=request.data.get('mail')
    medicinesForUser=MedicineForUser.objects.filter(mail=mail)
    for mfu in medicinesForUser:
        mfu.days={day:False for day in mfu.days}
        mfu.save()
    return Response("")

@api_view(['POST']) 
def getListMedicineNames(request):
    mail=request.data.get('mail')
    day=str(indexDay(request.data.get('day')))
    allNames =set(m.medicineName for m in Medicine.objects.all())
    medicineForUser=MedicineForUser.objects.filter(mail=mail)
    medicineForUserbyDay =list(filter(lambda mfu:day in mfu.days,medicineForUser))
    dayNames = set(m.medicineName for m in medicineForUserbyDay)
    return Response(allNames-dayNames)


#------------------------------- help fucntions ----------------------------------#


def medicineForUser(mail,levelNumber):
    MedicineForUser.objects.filter(mail=mail).delete()

    medicineBylevel=list(filter((lambda m:levelNumber in m.levels),Medicine.objects.all()))
    for medicine in medicineBylevel:
        mfu=MedicineForUser(mail=mail,
                            medicineName=medicine.medicineName,
                            count=medicine.count)
        mfu.days={day:False for day in stringDaysToIntDays(medicine.days)}
        mfu.save()


def listMedicines(mail):
    allmedicines=MedicineForUser.objects.filter(mail=mail)
    listMed=list([] for _ in range(7))
    for medicine in allmedicines:
        for day in medicine.days:
            tempMed={
                'day':day,
                'medicineName':medicine.medicineName,
                'count':medicine.count,
                'isActive':medicine.days[day]
            }
            listMed[int(day)-1].append(tempMed)
    return (listMed[-1:]+listMed[:-1])[::-1]


def stringDaysToIntDays(stingDays):
    return [indexDay(day) for day in stingDays]

def indexDay(stingDays):
    days=["ראשון","שני","שלישי","רבעי","חמישי","שישי","שבת"]
    return (days.index(stingDays)+1)


       
        


