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
from boyKidsProduct.models import boyCategoryTable, boyBrandTable, boyTagsTable, BoyProductTable, ImagesForBoyProduct
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink

# Create your views here.
def boys_product(request):
    category_data = boyCategoryTable.objects.all()
    brand_data = boyBrandTable.objects.all()
    tags_data = boyTagsTable.objects.all()
    boysProduct_data = BoyProductTable.objects.all()

    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()

    return render(request,'boysAllProductList.html',{   'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'boysProduct_data':boysProduct_data,
                                                        
                                                        'contact_table':contact_table,
                                                        'footer_about':footer_about,
                                                        'footer_categories':footer_categories,
                                                        'footer_usefullink':footer_usefullink, })

def boys_product_url_generator(request,id):
    if BoyProductTable.objects.filter(product_unique_id = id).exists():
        q = BoyProductTable.objects.get(product_unique_id = id)
        url = q.product_name 
        url = url.replace(" ", "-") 
        return redirect('/boysproduct-description/' + id + '/' + url  )
    else:
        return redirect('/not-found')


def boys_productDetail(request,id,url):
    if BoyProductTable.objects.filter(product_unique_id = id).exists():
        boys_data = BoyProductTable.objects.get(product_unique_id = id)
        boys_opt_img = ImagesForBoyProduct.objects.filter(man_product_id = boys_data).all()
        size = boys_data.product_size
        if (size!=''):
            size_list = boys_data.product_size.split(',')
            list_len = len(size_list)
        else:
            size_list =[]
            list_len = 0
        category_data = boyCategoryTable.objects.all()
        brand_data = boyBrandTable.objects.all()
        tags_data = boyTagsTable.objects.all()

        contact_table = contactTable.objects.all()
        footer_about = footerAbout.objects.all()
        footer_categories = footerCategories.objects.all()
        footer_usefullink = footerUsefulLink.objects.all()

        return render(request,'boysProductDetail.html',{'product_code':id, 
                                                        'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'boys_data':boys_data, 
                                                        'boys_opt_img':boys_opt_img, 
                                                        'size_list':size_list, 
                                                        'list_len':list_len,
                                                        
                                                        'contact_table':contact_table,
                                                        'footer_about':footer_about,
                                                        'footer_categories':footer_categories,
                                                        'footer_usefullink':footer_usefullink, })
    else:
        return HttpResponseRedirect('/not-found')

def boys_ajax_pagination(request):
    if (request.method == "POST"):
        limit_per_page = 9
        page_no = int(request.POST.get('page_no'))
        ctg = request.POST.get('active_ctg')
        ctg = boyCategoryTable.objects.get(category = ctg)

        offset = (page_no -1) * limit_per_page
        
        boys_data = BoyProductTable.objects.filter(product_category = ctg)[offset:offset+limit_per_page]
        boys_no = math.ceil(BoyProductTable.objects.count() / limit_per_page)

        data_json = serializers.serialize('json',boys_data)
        return JsonResponse(data={
            'data_json':data_json,
            'total_data':boys_no
        })

def boys_ajax_color_spliter(request):
    id =  request.POST.get('code')

    if BoyProductTable.objects.filter(product_unique_id = id).exists():
            q = BoyProductTable.objects.get(product_unique_id = id)
            color_list = q.product_color
            return JsonResponse(data={
                'color_list':color_list,
            })