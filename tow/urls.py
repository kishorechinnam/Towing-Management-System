from django.urls import path

from tow import views
from tow.views import CheckOutUpdateView

urlpatterns = [
    path('tow/checkin', views.VehicleCheckinView.as_view(), name='checkin'),
    path('', views.VehicleListView.as_view(), name='vehicle_list'),
    path('tow/towing_out/<int:pk>',
         CheckOutUpdateView.as_view(), name='towing_out'),

]
