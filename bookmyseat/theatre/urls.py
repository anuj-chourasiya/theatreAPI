from django.urls import include, path
from . import views


urlpatterns = [
    path('vacate/<int:seatnumber>',views.vacate_seat, name="vacate_seat"),
    path('get_info/<slug:field>',views.info_detail, name="get_info" ),
    path('occupy',views.occupy_seat,name="occupy_seat" ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

