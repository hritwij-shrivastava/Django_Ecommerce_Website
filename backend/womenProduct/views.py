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
from womenProduct.models import womenCategoryTable, womenBrandTable, womenTagsTable, WomenProductTable, ImagesForWomenProduct
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink

# Create your views here.

def product(request):
    category_data = womenCategoryTable.objects.all()
    brand_data = womenBrandTable.objects.all()
    tags_data = womenTagsTable.objects.all()
    womenProduct_data = WomenProductTable.objects.all()

    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()

    return render(request,'womenAllProductList.html',{  'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'womenProduct_data':womenProduct_data,

                                                        'contact_table':contact_table,
                                                        'footer_about':footer_about,
                                                        'footer_categories':footer_categories,
                                                        'footer_usefullink':footer_usefullink, })

def product_url_generator(request,id):
    if WomenProductTable.objects.filter(product_unique_id = id).exists():
        q = WomenProductTable.objects.get(product_unique_id = id)
        url = q.product_name 
        url = url.replace(" ", "-") 
        return redirect('/womenproduct-description/' + id + '/' + url  )
    else:
        return redirect('/not-found')


def productDetail(request,id,url):
    # q = request.GET['q']
    if WomenProductTable.objects.filter(product_unique_id = id).exists():
        women_data = WomenProductTable.objects.get(product_unique_id = id)
        women_opt_img = ImagesForWomenProduct.objects.filter(woman_product_id = women_data).all()
        size = women_data.product_size
        if (size!=''):
            size_list = women_data.product_size.split(',')
            list_len = len(size_list)
        else:
            size_list =[]
            list_len = 0
        category_data = womenCategoryTable.objects.all()
        brand_data = womenBrandTable.objects.all()
        tags_data = womenTagsTable.objects.all()

        contact_table = contactTable.objects.all()
        footer_about = footerAbout.objects.all()
        footer_categories = footerCategories.objects.all()
        footer_usefullink = footerUsefulLink.objects.all()
        return render(request,'womenProductDetail.html',{   'product_code':id, 
                                                            'category_data':category_data, 
                                                            'brand_data':brand_data, 
                                                            'tags_data':tags_data, 
                                                            'women_data':women_data, 
                                                            'women_opt_img':women_opt_img, 
                                                            'size_list':size_list, 
                                                            'list_len':list_len,
                                                            
                                                            'contact_table':contact_table,
                                                            'footer_about':footer_about,
                                                            'footer_categories':footer_categories,
                                                            'footer_usefullink':footer_usefullink, })
    else:
        return HttpResponseRedirect('/not-found')


def ajax_pagination(request):
    if (request.method == "POST"):
        limit_per_page = 9
        page_no = int(request.POST.get('page_no'))
        ctg = request.POST.get('active_ctg')
        ctg = womenCategoryTable.objects.get(category = ctg)

        offset = (page_no -1) * limit_per_page
        
        woman_data = WomenProductTable.objects.filter(product_category = ctg)[offset:offset+limit_per_page]
        woman_no = math.ceil(WomenProductTable.objects.count() / limit_per_page)

        data_json = serializers.serialize('json',woman_data)
        return JsonResponse(data={
            'data_json':data_json,
            'total_data':woman_no
        })

    return redirect('my-adminpage')


def ajax_color_spliter(request):
    id =  request.POST.get('code')

    if WomenProductTable.objects.filter(product_unique_id = id).exists():
            q = WomenProductTable.objects.get(product_unique_id = id)
            color_list = q.product_color
            return JsonResponse(data={
                'color_list':color_list,
            })