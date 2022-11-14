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
from menProduct.models import menCategoryTable, menBrandTable, menTagsTable, MenProductTable, ImagesForMenProduct
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink

# Create your views here.
def men_product(request):
    category_data = menCategoryTable.objects.all()
    brand_data = menBrandTable.objects.all()
    tags_data = menTagsTable.objects.all()
    menProduct_data = MenProductTable.objects.all()

    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()

    return render(request,'menAllProductList.html',{   'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'menProduct_data':menProduct_data,
                                                        'contact_table':contact_table,
                                                        'footer_about':footer_about,
                                                        'footer_categories':footer_categories,
                                                        'footer_usefullink':footer_usefullink, })

def men_product_url_generator(request,id):
    if MenProductTable.objects.filter(product_unique_id = id).exists():
        q = MenProductTable.objects.get(product_unique_id = id)
        url = q.product_name 
        url = url.replace(" ", "-") 
        return redirect('/menproduct-description/' + id + '/' + url  )
    else:
        return redirect('/not-found')


def men_productDetail(request,id,url):
    if MenProductTable.objects.filter(product_unique_id = id).exists():
        men_data = MenProductTable.objects.get(product_unique_id = id)
        men_opt_img = ImagesForMenProduct.objects.filter(man_product_id = men_data).all()
        size = men_data.product_size
        if (size!=''):
            size_list = men_data.product_size.split(',')
            list_len = len(size_list)
        else:
            size_list =[]
            list_len = 0
        category_data = menCategoryTable.objects.all()
        brand_data = menBrandTable.objects.all()
        tags_data = menTagsTable.objects.all()

        contact_table = contactTable.objects.all()
        footer_about = footerAbout.objects.all()
        footer_categories = footerCategories.objects.all()
        footer_usefullink = footerUsefulLink.objects.all()

        return render(request,'menProductDetail.html',{ 'product_code':id, 
                                                        'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'men_data':men_data, 
                                                        'men_opt_img':men_opt_img, 
                                                        'size_list':size_list, 
                                                        'list_len':list_len,
                                                        'contact_table':contact_table,
                                                        'footer_about':footer_about,
                                                        'footer_categories':footer_categories,
                                                        'footer_usefullink':footer_usefullink, })
    else:
        return HttpResponseRedirect('/not-found')

def men_ajax_pagination(request):
    if (request.method == "POST"):
        limit_per_page = 9
        page_no = int(request.POST.get('page_no'))
        ctg = request.POST.get('active_ctg')
        ctg = menCategoryTable.objects.get(category = ctg)

        offset = (page_no -1) * limit_per_page
        
        men_data = MenProductTable.objects.filter(product_category = ctg)[offset:offset+limit_per_page]
        men_no = math.ceil(MenProductTable.objects.count() / limit_per_page)

        data_json = serializers.serialize('json',men_data)
        return JsonResponse(data={
            'data_json':data_json,
            'total_data':men_no
        })

def men_ajax_color_spliter(request):
    id =  request.POST.get('code')

    if MenProductTable.objects.filter(product_unique_id = id).exists():
            q = MenProductTable.objects.get(product_unique_id = id)
            color_list = q.product_color
            return JsonResponse(data={
                'color_list':color_list,
            })