from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
# Create your models here.
class Seat(models.Model):
    seatnumber=models.IntegerField(primary_key=True)
    isavailable = models.BooleanField(default=True)
    
    def nextseatnumber():
        sn=Seat.objects.values_list('seatnumber')
        #print("sn=",sn)
        l1=Seat.objects.values_list('seatnumber','isavailable')
        for seat in range(1,int(settings.MAX_OCCUPANCY)+1):
            #print("seatno",seat)
            if ((seat,) not in sn):
                #print("inside if")
                m=Seat(seatnumber=seat,isavailable='False')
                m.save()
                return seat
            elif (seat,True) in l1:
                #print("inside elif")
                ob=Seat.objects.get(pk=seat)
                ob.isavailable=False
                ob.save()
                return seat
        return -1

  
        

class Info(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60,unique=True)
    seatnumber = models.ForeignKey(Seat,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

