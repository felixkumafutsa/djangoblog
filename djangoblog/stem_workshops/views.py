from django.views import generic
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def electric_propella_car(request):
    return render(request, 'stem_workshops/electric_propella_car.html')


def electricity_and_magnetism(request):
    return render(request, 'stem_workshops/electricity_and_magnetism.html')

def intro_to_coding(request):
    return render(request, 'stem_workshops/intro_to_coding.html')

def renewable_energy(request):
    return render(request, 'stem_workshops/renewable_energy.html')

def stop_motion_animation(request):
    return render(request, 'stem_workshops/stop_motion_animation.html')

def structural_engineering(request):
    return render(request, 'stem_workshops/structural_engineering.html')

