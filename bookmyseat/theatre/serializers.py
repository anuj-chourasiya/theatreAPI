from rest_framework import serializers

from .models import Info,Seat

class OccupySerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('name', 'uid','seatnumber')
        extra_kwargs = {
         'seatnumber': {'read_only': True}
         }


class GetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info,Seat
        fields = ('name', 'uid','seatnumber')
        