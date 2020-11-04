from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
import os
import sys
import urllib.request
from .__code import *

# Create your views here.


def searchbook(request):
    bookcontent = request.GET['bookcontent']
    client_id = "t6FyW7KHzTiC0x5_r2D_"
    client_secret = "Pg2Jx6DUFx"
    encText = urllib.parse.quote(bookcontent)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",naver_id)
    request.add_header("X-Naver-Client-Secret",naver_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(type(response_body))
        print(type(response_body.decode('utf-8')))
        return HttpResponse(response_body.decode('utf-8'))
    else:
        return HttpResponse("Error Code:" + rescode)


def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants': restaurants}
    return render(request, 'shareRes/index.html', content)


def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'restaurant': restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)


def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/restaurantCreate.html', content)


def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories': categories,'restaurant': restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)


def Delete_restaurant(request):

    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id=res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))


def Update_restaurant(request):
    resId = request.POST['resId']
    chage_category = Category.objects.get(id = request.POST["resCategory"])
    restaurant = Restaurant.objects.get(id = resId)
    restaurant.restaurant_name = request.POST["resTitle"]
    restaurant.restaurant_link = request.POST["resLink"]
    restaurant.restaurant_content = request.POST["resContent"]
    restaurant.restaurant_keyword = request.POST["resLoc"]
    restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id': resId}))


def create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id=category_id)
    name = request.POST['resContent']
    link = request.POST['resLoc']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link, restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))


def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)


def create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))


def delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))