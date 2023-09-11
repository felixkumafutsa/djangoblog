from . import views
from django.urls import path

urlpatterns = [
    path('electric_propella_car', views.electric_propella_car, name='electric_propella_car'),
    path('electricity_and_magnetism', views.electricity_and_magnetism, name='electricity_and_magnetism'),
    path('intro_to_coding', views.intro_to_coding, name='intro_to_coding'),
    path('renewable_energy', views.renewable_energy, name='renewable_energy'),
    path('stop_motion_animation', views.stop_motion_animation, name='stop_motion_animation'),
    path('structural_engineering', views.structural_engineering, name='structural_engineering'),
]