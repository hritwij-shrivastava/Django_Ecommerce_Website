from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.models import SliderImages, HeaderText, ProductID, UpSliderImages, LogoImages, AdVideo, InstaImages
from womenProduct.models import womenCategoryTable, womenBrandTable, womenTagsTable, WomenProductTable, ImagesForWomenProduct
from menProduct.models import menCategoryTable, menBrandTable, menTagsTable, MenProductTable, ImagesForMenProduct
from girlKidsProduct.models import girlCategoryTable, girlBrandTable, girlTagsTable, GirlProductTable, ImagesForGirlProduct
from boyKidsProduct.models import boyCategoryTable, boyBrandTable, boyTagsTable, BoyProductTable, ImagesForBoyProduct
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink


def index(request):
    Slider_Images = SliderImages.objects.all()
    Slider_Count = SliderImages.objects.count()

    headerText = HeaderText.objects.all()

    product_for_filter = ProductID.objects.all()

    UpSlider_Images = UpSliderImages.objects.all()
    UpSlider_Count = UpSliderImages.objects.count()

    Logo_Images = LogoImages.objects.all()
    Ad_Video = AdVideo.objects.all()
    Insta_Images = InstaImages.objects.all()

    arr =[]
    for pId in product_for_filter:
        arr.append(pId.pid)

    women_Product = WomenProductTable.objects.filter(product_unique_id__in = arr)
    men_Product = MenProductTable.objects.filter(product_unique_id__in = arr)
    girlkid_product = GirlProductTable.objects.filter(product_unique_id__in = arr)
    boykid_product = BoyProductTable.objects.filter(product_unique_id__in = arr)

    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()

    return render(request,'index.html',{'Slider_Images':Slider_Images,
                                        'range': range(0,Slider_Count),
                                        'UpSlider_Images':UpSlider_Images,
                                        'uprange': range(0,UpSlider_Count),
                                        'headerText':headerText,
                                        'women_product': women_Product,
                                        'men_product':men_Product,
                                        'girlkid_product':girlkid_product,
                                        'boykid_product':boykid_product,
                                        'Logo_Images':Logo_Images,
                                        'Ad_Video':Ad_Video,
                                        'Insta_Images':Insta_Images,
                                        
                                        'contact_table':contact_table,
                                        'footer_about':footer_about,
                                        'footer_categories':footer_categories,
                                        'footer_usefullink':footer_usefullink,})