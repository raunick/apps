from django.urls import path
from . import views

urlpatterns = [
    path('recycling-info/', views.recycling_info_view, name='recycling_info'),
    path('recycling/', views.recycling_info_view2, name='recycling'),
]
