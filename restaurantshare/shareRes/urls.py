from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('restaurantDetail/', restaurantDetail, name="resDetailPage"),
    path('restaurantCreate/', restaurantCreate, name="resCreatePage"),
    path('categoryCreate/', categoryCreate, name="cateCreatePage"),
    path('categoryCreate/create', create_category, name="cateCreate"),
    path('categoryCreate/delete', delete_category, name="cateDelete"),
]