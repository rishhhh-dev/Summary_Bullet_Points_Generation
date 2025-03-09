from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('generate-summary/',generate_summary,name='generate_summary'),
    path('generate-bullet-points/',generate_bullet_points,name='generate_bullets')
]