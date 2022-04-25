from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import CheckInForm, CheckOutForm
from .models import Vehicles, AllocatedVehicles


class VehicleListView(LoginRequiredMixin, ListView):
    model = AllocatedVehicles
    template_name = 'vehicles/vehicle_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allocated_vehicles = AllocatedVehicles.objects.all()
        context['allocated_vehicles'] = allocated_vehicles.filter(towing_out=False)
        context['available_vehicles'] = Vehicles.objects.filter(assigned=False).count()
        return context


class VehicleCheckinView(LoginRequiredMixin, CreateView):
    form_class = CheckInForm
    template_name = 'vehicles/checkin.html'


class CheckOutUpdateView(LoginRequiredMixin, UpdateView):
    model = AllocatedVehicles
    success_url = reverse_lazy('vehicle_list')
    form_class = CheckOutForm
    template_name = 'vehicles/check_out.html'


