from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('restaurantDetail/delete', Delete_restaurant, name='resDelete'),
    path('restaurantDetail/<str:res_id>', restaurantDetail, name='resDetailPage'),
    path('restaurantDetail/updatePage/update', Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>', restaurantUpdate, name='resUpdatePage'),
    path('restaurantDetail/', restaurantDetail, name="resDetailPage"),
    path('restaurantCreate/', restaurantCreate, name="resCreatePage"),
    path('restaurantCreate/create', create_restaurant, name="resCreate"),
    path('categoryCreate/', categoryCreate, name="cateCreatePage"),
    path('categoryCreate/create', create_category, name="cateCreate"),
    path('categoryCreate/delete', delete_category, name="cateDelete"),
    path('searchbook/', searchbook, name="searchbook")
]