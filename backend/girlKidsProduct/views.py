from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.sites.models import Site 
# from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import math
import random
import json
from girlKidsProduct.models import girlCategoryTable, girlBrandTable, girlTagsTable, GirlProductTable, ImagesForGirlProduct
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink

def girls_product(request):
    category_data = girlCategoryTable.objects.all()
    brand_data = girlBrandTable.objects.all()
    tags_data = girlTagsTable.objects.all()
    womanProduct_data = GirlProductTable.objects.all()

    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()    
    return render(request,'girlsAllProductList.html',{  'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'girlsProduct_data':womanProduct_data,
                                                        
                                                        'contact_table':contact_table,
                                                        'footer_about':footer_about,
                                                        'footer_categories':footer_categories,
                                                        'footer_usefullink':footer_usefullink,})

def girls_product_url_generator(request,id):
    if GirlProductTable.objects.filter(product_unique_id = id).exists():
        q = GirlProductTable.objects.get(product_unique_id = id)
        url = q.product_name 
        url = url.replace(" ", "-") 
        return HttpResponseRedirect('/girlsproduct-description/' + id + '/' + url  )
    else:
        return HttpResponseRedirect('/not-found')


def girls_productDetail(request,id,url):
    # q = request.GET['q']
    if GirlProductTable.objects.filter(product_unique_id = id).exists():
        girls_data = GirlProductTable.objects.get(product_unique_id = id)
        girls_opt_img = ImagesForGirlProduct.objects.filter(woman_product_id = girls_data).all()
        size = girls_data.product_size
        if (size!=''):
            size_list = girls_data.product_size.split(',')
            list_len = len(size_list)
        else:
            size_list =[]
            list_len = 0
        category_data = girlCategoryTable.objects.all()
        brand_data = girlBrandTable.objects.all()
        tags_data = girlTagsTable.objects.all()

        contact_table = contactTable.objects.all()
        footer_about = footerAbout.objects.all()
        footer_categories = footerCategories.objects.all()
        footer_usefullink = footerUsefulLink.objects.all()

        return render(request,'girlsProductDetail.html',{'product_code':id, 
                                                            'category_data':category_data, 
                                                            'brand_data':brand_data, 
                                                            'tags_data':tags_data, 
                                                            'girls_data':girls_data, 
                                                            'girls_opt_img':girls_opt_img, 
                                                            'size_list':size_list, 
                                                            'list_len':list_len,

                                                            'contact_table':contact_table,
                                                            'footer_about':footer_about,
                                                            'footer_categories':footer_categories,
                                                            'footer_usefullink':footer_usefullink,})
    else:
        return HttpResponseRedirect('/not-found')
    

def girls_ajax_pagination(request):
    if (request.method == "POST"):
        limit_per_page = 9
        page_no = int(request.POST.get('page_no'))
        ctg = request.POST.get('active_ctg')
        ctg = girlCategoryTable.objects.get(category = ctg)

        offset = (page_no -1) * limit_per_page
        
        girls_data = GirlProductTable.objects.filter(product_category = ctg)[offset:offset+limit_per_page]
        girls_no = math.ceil(GirlProductTable.objects.count() / limit_per_page)

        data_json = serializers.serialize('json',girls_data)
        return JsonResponse(data={
            'data_json':data_json,
            'total_data':girls_no
        })

def girls_ajax_color_spliter(request):
    id =  request.POST.get('code')

    if GirlProductTable.objects.filter(product_unique_id = id).exists():
            q = GirlProductTable.objects.get(product_unique_id = id)
            color_list = q.product_color
            return JsonResponse(data={
                'color_list':color_list,
            })