from .serializers import OccupySerializer,GetInfoSerializer
from .models import Info,Seat
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response


@api_view(['POST',])
def occupy_seat(request):
    serializer_class=OccupySerializer
    if request.method == 'POST':
        g = request.data
        serializer = OccupySerializer(data=g)
        if serializer.is_valid():
            data={}
            res=Seat.nextseatnumber()
            if res==-1:
                return Response({'sorry':'capacity is full !'})
            else:
                ob=Seat.objects.get(pk=res)
                person=Info(name=g['name'],seatnumber=ob)
                person.save()
                data['seatnumber']=res
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def vacate_seat(request,seatnumber):  
    print("inside")
    try:
        seat=Seat.objects.get(pk=seatnumber)
    except:
        return Response("object not found", status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation=seat.delete()
        data={}
        if operation:
            data["success"]="delete successful"
        else:
            data["failure"]="delete failed"
        return Response(data)
