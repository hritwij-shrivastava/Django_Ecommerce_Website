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
from home.models import SliderImages, HeaderText, ProductID, UpSliderImages, LogoImages, AdVideo, InstaImages
from about.models import aboutSliderImages, aboutHeaderText, companyData, vision, leadership
from contact.models import contactTable, userMessage, footerAbout, footerCategories, footerUsefulLink
from womenProduct.models import womenCategoryTable, womenBrandTable, womenTagsTable, WomenProductTable, ImagesForWomenProduct
from menProduct.models import menCategoryTable, menBrandTable, menTagsTable, MenProductTable, ImagesForMenProduct
from girlKidsProduct.models import girlCategoryTable, girlBrandTable, girlTagsTable, GirlProductTable, ImagesForGirlProduct
from boyKidsProduct.models import boyCategoryTable, boyBrandTable, boyTagsTable, BoyProductTable, ImagesForBoyProduct
from blog.models import BlogPost



#<------------------------------Admin Home Start------------------------------------------------>

def my_admin_page(request):
    if request.user.is_authenticated:
        return redirect('admin-home')
    else:
        return render(request,'admin2/login.html')

def my_admin_pagelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(request, user)
            return redirect('admin-home')
        else:
            messages.error(request, "Invalid Credentials,Please try again")
            return redirect('my-adminpage')
    
    return redirect('my-adminpage')

def my_admin_pagelogout(request):
    logout(request)
    return redirect('my-adminpage')

def admin_home(request):
    if request.user.is_authenticated:
        slider_images = SliderImages.objects.all()
        slide_count = SliderImages.objects.count()

        header_text = HeaderText.objects.all()
        header_count = HeaderText.objects.count()

        product_id = ProductID.objects.all()
        product_id_count = ProductID.objects.count()

        upSlider_images = UpSliderImages.objects.all()
        upSlider_images_count = UpSliderImages.objects.count()

        logo_images = LogoImages.objects.all()
        logo_images_count = LogoImages.objects.count()

        ad_video = AdVideo.objects.all()
        ad_video_count = AdVideo.objects.count()

        insta_images = InstaImages.objects.all()
        insta_images_count = InstaImages.objects.count()

        return render(request,'admin2/home.html',{  'slider_images':slider_images,
                                                    'slide_count':slide_count,
                                                    'header_text':header_text,
                                                    'header_count':header_count,
                                                    'product_id':product_id,
                                                    'product_id_count':product_id_count,
                                                    'upSlider_images':upSlider_images,
                                                    'upSlider_images_count':upSlider_images_count,
                                                    'logo_images':logo_images,
                                                    'logo_images_count':logo_images_count,
                                                    'ad_video':ad_video,
                                                    'ad_video_count':ad_video_count,
                                                    'insta_images':insta_images,
                                                    'insta_images_count':insta_images_count})
    else:
        return redirect('my-adminpage')

def updateSlider(request):
    if request.method == 'POST':
        slider_img = request.FILES.getlist('slider_img_input')

        for img in slider_img:
            updateSlider = SliderImages(sliderImage = img)
            updateSlider.save()
        response_data={
            'title' : 'Images added successfullly'
        }
        return JsonResponse(response_data, safe=False)
    
    return redirect('my-adminpage')

def headerText(request):
    if request.method == 'POST':
        headerText = HeaderText.objects.all()
        headerText.delete()
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        headerText = HeaderText(title = title,desc = desc)
        headerText.save()
        response_data={
            'title' : 'Text added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def productID(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        productID = ProductID(pid = pid)
        productID.save()
        response_data={
            'title' : 'Text added successfully'
        }
        return JsonResponse(response_data, safe=False)
    
    return redirect('my-adminpage')

def updateUpSlider(request):
    if request.method == 'POST':
        upsliderImage = request.FILES.getlist('upslider_img_input')

        for img in upsliderImage:
            updateUpSlider = UpSliderImages(upsliderImage = img)
            updateUpSlider.save()
        response_data={
            'title' : 'Images added successfullly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def logoImage(request):
    if request.method == 'POST':
        logo_image = request.FILES.getlist('logo_img_input')

        for img in logo_image:
            logoImage = LogoImages(logoImage = img)
            logoImage.save()
        response_data={
            'title' : 'Images added successfullly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def ad_Video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        ad_Video = AdVideo(url = url)
        ad_Video.save()
        response_data={
            'title' : 'Text added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def insta_Image(request):
    if request.method == 'POST':
        insta = request.FILES.getlist('insta_img_input')

        for img in insta:
            insta_Image = InstaImages(instaImage = img)
            insta_Image.save()
        response_data={
            'title' : 'Images added successfullly'
        }
        return JsonResponse(response_data, safe=False)
    
    return redirect('my-adminpage')


#<---------------------------------------------Admin Home End----------------------------------------------->



#<---------------------------------------------Admin About Start------------------------------------------->


def admin_about(request):
    if request.user.is_authenticated:
        about_slider_images = aboutSliderImages.objects.all()
        about_slider_images_count = aboutSliderImages.objects.count()

        about_header_text = aboutHeaderText.objects.all()
        aboutHeaderText_count = aboutHeaderText.objects.count()

        company_data = companyData.objects.all()
        company_data_count = companyData.objects.count()

        vision_data = vision.objects.all()
        vision_count = vision.objects.count()

        leadership_data = leadership.objects.all()
        leadership_count = leadership.objects.count()

        return render(request,'admin2/about.html',{ 'about_slider_images':about_slider_images,
                                                    'about_slider_images_count':about_slider_images_count,
                                                    'about_header_text':about_header_text,
                                                    'aboutHeaderText_count':aboutHeaderText_count,
                                                    'company_data':company_data,
                                                    'company_data_count':company_data_count,
                                                    'vision_data':vision_data,
                                                    'vision_count':vision_count,
                                                    'leadership_data':leadership_data,
                                                    'leadership_count':leadership_count})
    else:
        return redirect('my-adminpage')

def about_slider(request):
    if request.method == 'POST':
        slider_img = request.FILES.getlist('slider_img_input')

        for img in slider_img:
            about_slider = aboutSliderImages(sliderImage = img)
            about_slider.save()
        response_data={
            'title' : 'Images added successfullly'
        }
        return JsonResponse(response_data, safe=False)
    
    return redirect('my-adminpage')

def about_header(request):
    if request.method == 'POST':
        about_header = aboutHeaderText.objects.all()
        about_header.delete()
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        about_header = aboutHeaderText(title = title,desc = desc)
        about_header.save()
        response_data={
            'title' : 'Text added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def about_companydata(request):
    if request.method == 'POST':
        about_companydata = companyData.objects.all()
        about_companydata.delete()

        data1 = request.POST.get('data1')
        title_data1 = request.POST.get('title_data1')

        data2 = request.POST.get('data2')
        title_data2 = request.POST.get('title_data2')

        data3 = request.POST.get('data3')
        title_data3 = request.POST.get('title_data3')

        data4 = request.POST.get('data4')
        title_data4 = request.POST.get('title_data4')

        about_companydata = companyData(data1 = data1, 
                                        title_data1 = title_data1, 
                                        data2 = data2, 
                                        title_data2 = title_data2, 
                                        data3 = data3, 
                                        title_data3 = title_data3, 
                                        data4 = data4, 
                                        title_data4 = title_data4)
        about_companydata.save()
        response_data={
            'title' : 'Item added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def about_vision(request):
    if request.method == 'POST':
        about_vision = vision.objects.all()
        about_vision.delete()
        visionImage = request.FILES.get('visionImage')
        vision_desc = request.POST.get('vision_desc')
        about_vision = vision(visionImage = visionImage, vision_desc = vision_desc)
        about_vision.save()
        response_data={
            'title' : 'Text added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def about_leadership(request):
    if request.method == 'POST':
        leaderImage = request.FILES.get('leaderImage')
        leader_name = request.POST.get('leader_name')
        leader_designation = request.POST.get('leader_designation')
        leader_desc = request.POST.get('leader_desc')
        leader_social_media = request.POST.get('leader_social_media')

        about_leadership = leadership(  leaderImage = leaderImage, 
                                        leader_name = leader_name, 
                                        leader_designation=leader_designation,
                                        leader_desc = leader_desc,
                                        leader_social_media = leader_social_media)
        about_leadership.save()
        response_data={
            'title' : 'Item added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

#<---------------------------------------------Admin About End---------------------------------------------->


#<---------------------------------------------Admin Contact Start------------------------------------------->

def admin_contact(request):
    if request.user.is_authenticated:
        contact_table = contactTable.objects.all()
        contact_table_count = contactTable.objects.count()

        user_message = userMessage.objects.all()
        user_message_count = userMessage.objects.count()

        footer_about = footerAbout.objects.all()
        footer_about_count = footerAbout.objects.count()

        footer_categories = footerCategories.objects.all()
        footer_categories_count = footerCategories.objects.count()

        footer_usefullink = footerUsefulLink.objects.all()
        footer_usefullink_count = footerUsefulLink.objects.count()

        return render(request,'admin2/contact.html',{    'contact_table':contact_table,
                                                        'contact_table_count':contact_table_count,
                                                        'user_message':user_message,
                                                        'user_message_count':user_message_count,
                                                        'footer_about':footer_about,
                                                        'footer_about_count':footer_about_count,
                                                        'footer_categories':footer_categories,
                                                        'footer_categories_count':footer_categories_count,
                                                        'footer_usefullink':footer_usefullink,
                                                        'footer_usefullink_count':footer_usefullink_count})
    else:
        return redirect('my-adminpage')

def contact_info(request):
    if request.method == 'POST':
        contact_info = contactTable.objects.all()
        contact_info.delete()

        background_img = request.FILES.get('background_img')
        address = request.POST.get('address')
        phoneNo = request.POST.get('phoneNo')
        workingHour1 = request.POST.get('workingHour1')
        workingHour2 = request.POST.get('workingHour2')
        facebook_url = request.POST.get('facebook_url')
        twitter_url = request.POST.get('twitter_url')
        insta_url = request.POST.get('insta_url')
        linkedin_url = request.POST.get('linkedin_url')

        contact_info = contactTable(background_img = background_img, 
                                    address = address, 
                                    phoneNo = phoneNo,
                                    workingHour1 = workingHour1,
                                    workingHour2 = workingHour2,
                                    facebook_url = facebook_url,
                                    twitter_url = twitter_url,
                                    insta_url = insta_url,
                                    linkedin_url = linkedin_url)
        contact_info.save()
        response_data={
            'title' : 'Item added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')


def footer_about(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')

        footer_about = footerAbout(title = title, url = url)
        footer_about.save()
        response_data={
            'title' : 'Item added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def footer_category(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')

        footer_category = footerCategories(title = title, url = url)
        footer_category.save()
        response_data={
            'title' : 'Item added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def footer_useful(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')

        footer_useful = footerUsefulLink(title = title, url = url)
        footer_useful.save()
        response_data={
            'title' : 'Item added successfully'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

#<---------------------------------------------Admin Contact End--------------------------------------------->

#<---------------------------------------------Admin Women Zone Start---------------------------------------->

def admin_women(request):                                        #Check user is authenticated or not
    if request.user.is_authenticated:                            #If User is logged in 
        category_data = womenCategoryTable.objects.all()         #Extract Each data from all table and count number of items in that table 
        ctg_no = womenCategoryTable.objects.count()

        brand_data = womenBrandTable.objects.all()
        bnd_no = womenBrandTable.objects.count()

        tags_data = womenTagsTable.objects.all()
        tag_no = womenTagsTable.objects.count()

        woman_data = WomenProductTable.objects.all()
        woman_no = WomenProductTable.objects.count()

        images_data = ImagesForWomenProduct.objects.all()
        
                                                                #Pass all the extracted result to the template
        return render(request,'admin2/womenzone.html',{'category_data':category_data, 
                                                   'brand_data':brand_data, 
                                                   'tags_data':tags_data, 
                                                   'woman_data':woman_data, 
                                                   'images_data':images_data, 
                                                   'ctg_no':ctg_no, 
                                                   'bnd_no':bnd_no,
                                                   'tag_no':tag_no,
                                                   'woman_no':woman_no })	
    
    return redirect('my-adminpage')                             #if user is not logged in then redirect it to the login page


def categoryClass(request):                                     #In this class I am getting data from admin page through javascript and then submitting it to the table
    if (request.method == "POST"):
        category_name = request.POST.get('category')
        category_item_no = 0                                    #Initializing number of item with zero as no product is related to this class because here I am just creating this class

        categoryClass = womenCategoryTable(category=category_name,category_item_no=category_item_no, date=datetime.today())
        categoryClass.save()
        response_data={
            'title' : 'Category added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def brandClass(request):
    if (request.method == "POST"):
        brand_name = request.POST.get('brand')
        brand_item_no = 0
        brand_img = request.FILES.get('brand_img')
        brandClass = womenBrandTable(brand=brand_name, brand_item_no=brand_item_no, brand_img=brand_img, date=datetime.today())
        brandClass.save()
        response_data={
            'title' : 'Brand added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def tagsClass(request):
    if (request.method == "POST"):
        tags_name = request.POST.get('tags')
        tags_no_item = 0
        tagsClass = womenTagsTable(tags=tags_name, tags_no_item=tags_no_item, date=datetime.today())
        tagsClass.save()
        response_data={
            'title' : 'Tags added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def womanProductClass(request):                                                     #In this class I am getting data from admin pannel for item related to women products
    if (request.method == "POST"):
        product_unique_id = random.randint(123456,9876543)                          #Here I am giving every product a unique id to access that particular product later
        product_name = request.POST.get('product_name')
        product_id = request.POST.get('product_id')                                 #This id will be the product id which is company using
        product_category = request.POST.get('product_ctg')

        if(product_category==""):                                                    #Here I am checking wheather any category is assigned to that product or not
            ctg_id = None
        else:
            ctg_id = womenCategoryTable.objects.get(category=product_category)        #Now I am storing the foreign key of that category into this product to access product related to that category

        product_brand = request.POST.get('product_brand')
        if(product_brand==""):
            bnd_id = None
        else:
            bnd_id = womenBrandTable.objects.get(brand=product_brand)
    
        product_tag = request.POST.get('product_tags')
        if(product_tag==""):
            tag_id = None
        else:
            tag_id = womenTagsTable.objects.get(tags=product_tag)

        product_size = request.POST.get('size')
        product_specification = request.POST.get('product_spec')
        product_color = request.POST.get('product_color')
        product_img = request.FILES.get('product_img')
        product_img_no = request.POST.get('product_img_no')
        product_opt_img = request.FILES.getlist('product_opt_img')

        womanProductClass = WomenProductTable(  product_unique_id = product_unique_id, 
                                                product_name = product_name, 
                                                product_id = product_id, 
                                                product_category = ctg_id, 
                                                product_brand = bnd_id, 
                                                product_tag = tag_id, 
                                                product_size = product_size, 
                                                product_specification = product_specification,  
                                                product_color = product_color, 
                                                product_img = product_img, 
                                                product_img_no = product_img_no, 
                                                date = datetime.today())
        womanProductClass.save()

        wp = WomenProductTable.objects.get(product_unique_id = product_unique_id)       #Here I am getting the Id(table id) of the product

        for f in product_opt_img:
            womanProductClass = ImagesForWomenProduct(product_unique_id=product_unique_id,product_opt_img=f,woman_product_id=wp)            #So that I can store the foreign key with all optioal images related to that product
            womanProductClass.save()
        
        response_data={
            'title' : 'Product added successfuly'
        }

        update_all_item(product_category,product_brand,product_tag)             #Now I am calling this function so that it can indicate to that category, brand or tag that this particular product is related to that product
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')


def update_all_item(ctg,bnd,tag):
    if (ctg!=''):
        ctg = womenCategoryTable.objects.get(category = ctg)
        category_item_no = WomenProductTable.objects.filter(product_category = ctg).count()
        womenCategoryTable.objects.filter(category = ctg).update(category_item_no = category_item_no)
    
    if (bnd!=''):
        bnd = womenBrandTable.objects.get(brand = bnd)
        brand_item_no = WomenProductTable.objects.filter(product_brand = bnd).count()
        womenBrandTable.objects.filter(brand = bnd).update(brand_item_no = brand_item_no)
    
    if (tag!=''):
        tag = womenTagsTable.objects.get(tags = tag)
        tags_no_item = WomenProductTable.objects.filter(product_tag = tag).count()
        womenTagsTable.objects.filter(tags = tag).update(tags_no_item = tags_no_item)



#<---------------------------------------------Admin Women Zone End------------------------------------------>

#<---------------------------------------------Admin Men Zone Start------------------------------------------>
def admin_men(request):
    if request.user.is_authenticated:
        category_data = menCategoryTable.objects.all()
        ctg_no = menCategoryTable.objects.count()

        brand_data = menBrandTable.objects.all()
        bnd_no = menBrandTable.objects.count()

        tags_data = menTagsTable.objects.all()
        tag_no = menTagsTable.objects.count()

        woman_data = MenProductTable.objects.all()
        woman_no = MenProductTable.objects.count()

        images_data = ImagesForMenProduct.objects.all()
                
        return render(request,'admin2/menzone.html',{   'category_data':category_data, 
                                                        'brand_data':brand_data, 
                                                        'tags_data':tags_data, 
                                                        'woman_data':woman_data, 
                                                        'images_data':images_data, 
                                                        'ctg_no':ctg_no, 
                                                        'bnd_no':bnd_no,
                                                        'tag_no':tag_no,
                                                        'woman_no':woman_no })	
    else:
        return redirect('my-adminpage')


def men_categoryClass(request):
    if (request.method == "POST"):
        category_name = request.POST.get('category')
        category_item_no = 0
        categoryClass = menCategoryTable(category=category_name,category_item_no=category_item_no, date=datetime.today())
        categoryClass.save()
        response_data={
            'title' : 'Category added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def men_brandClass(request):
    if (request.method == "POST"):
        brand_name = request.POST.get('brand')
        brand_item_no = 0
        brand_img = request.FILES.get('brand_img')
        brandClass = menBrandTable(brand=brand_name, brand_item_no=brand_item_no, brand_img=brand_img, date=datetime.today())
        brandClass.save()
        response_data={
            'title' : 'Brand added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def men_tagsClass(request):
    if (request.method == "POST"):
        tags_name = request.POST.get('tags')
        tags_no_item = 0
        tagsClass = menTagsTable(tags=tags_name, tags_no_item=tags_no_item, date=datetime.today())
        tagsClass.save()
        response_data={
            'title' : 'Tags added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def MenProductClass(request):
    if (request.method == "POST"):
        product_unique_id = random.randint(123456,9876543)
        product_name = request.POST.get('product_name')
        product_id = request.POST.get('product_id')
        product_category = request.POST.get('product_ctg')

        if(product_category==""):
            ctg_id = None
        else:
            ctg_id = menCategoryTable.objects.get(category=product_category)

        product_brand = request.POST.get('product_brand')
        if(product_brand==""):
            bnd_id = None
        else:
            bnd_id = menBrandTable.objects.get(brand=product_brand)
    
        product_tag = request.POST.get('product_tags')
        if(product_tag==""):
            tag_id = None
        else:
            tag_id = menTagsTable.objects.get(tags=product_tag)

        product_size = request.POST.get('size')
        product_specification = request.POST.get('product_spec')
        product_color = request.POST.get('product_color')
        product_img = request.FILES.get('product_img')
        product_img_no = request.POST.get('product_img_no')
        product_opt_img = request.FILES.getlist('product_opt_img')
        MenProductClass = MenProductTable(  product_unique_id = product_unique_id, 
                                            product_name = product_name, 
                                            product_id = product_id, 
                                            product_category = ctg_id, 
                                            product_brand = bnd_id, 
                                            product_tag = tag_id, 
                                            product_size = product_size, 
                                            product_specification = product_specification,  
                                            product_color = product_color, 
                                            product_img = product_img, 
                                            product_img_no = product_img_no, 
                                            date = datetime.today())
        MenProductClass.save()

        wp = MenProductTable.objects.get(product_unique_id = product_unique_id)
        for f in product_opt_img:
            MenProductClass = ImagesForMenProduct(product_unique_id=product_unique_id,product_opt_img=f,man_product_id=wp)
            MenProductClass.save()
        
        response_data={
            'title' : 'Product added successfuly'
        }

        men_update_all_item(product_category,product_brand,product_tag)
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')


def men_update_all_item(ctg,bnd,tag):
    if (ctg!=''):
        ctg = menCategoryTable.objects.get(category = ctg)
        category_item_no = MenProductTable.objects.filter(product_category = ctg).count()
        menCategoryTable.objects.filter(category = ctg).update(category_item_no = category_item_no)
    
    if (bnd!=''):
        bnd = menBrandTable.objects.get(brand = bnd)
        brand_item_no = MenProductTable.objects.filter(product_brand = bnd).count()
        menBrandTable.objects.filter(brand = bnd).update(brand_item_no = brand_item_no)
    
    if (tag!=''):
        tag = menTagsTable.objects.get(tags = tag)
        tags_no_item = MenProductTable.objects.filter(product_tag = tag).count()
        menTagsTable.objects.filter(tags = tag).update(tags_no_item = tags_no_item)

#<---------------------------------------------Admin Men Zone End------------------------------------------>


#<---------------------------------------------Admin Girls Zone Start-------------------------------------->

def admin_girls(request):
    if request.user.is_authenticated:
        category_data = girlCategoryTable.objects.all()
        ctg_no = girlCategoryTable.objects.count()

        brand_data = girlBrandTable.objects.all()
        bnd_no = girlBrandTable.objects.count()

        tags_data = girlTagsTable.objects.all()
        tag_no = girlTagsTable.objects.count()

        woman_data = GirlProductTable.objects.all()
        woman_no = GirlProductTable.objects.count()

        images_data = ImagesForGirlProduct.objects.all()
                
        return render(request,'admin2/girlkidzone.html',{   'category_data':category_data, 
                                                            'brand_data':brand_data, 
                                                            'tags_data':tags_data, 
                                                            'woman_data':woman_data, 
                                                            'images_data':images_data, 
                                                            'ctg_no':ctg_no, 
                                                            'bnd_no':bnd_no,
                                                            'tag_no':tag_no,
                                                            'woman_no':woman_no })	
    
    else:
        return redirect('my-adminpage')

def girls_categoryClass(request):
    if (request.method == "POST"):
        category_name = request.POST.get('category')
        category_item_no = 0
        categoryClass = girlCategoryTable(category=category_name,category_item_no=category_item_no, date=datetime.today())
        categoryClass.save()
        response_data={
            'title' : 'Category added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def girls_brandClass(request):
    if (request.method == "POST"):
        brand_name = request.POST.get('brand')
        brand_item_no = 0
        brand_img = request.FILES.get('brand_img')
        brandClass = girlBrandTable(brand=brand_name, brand_item_no=brand_item_no, brand_img=brand_img, date=datetime.today())
        brandClass.save()
        response_data={
            'title' : 'Brand added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def girls_tagsClass(request):
    if (request.method == "POST"):
        tags_name = request.POST.get('tags')
        tags_no_item = 0
        tagsClass = girlTagsTable(tags=tags_name, tags_no_item=tags_no_item, date=datetime.today())
        tagsClass.save()
        response_data={
            'title' : 'Tags added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')

def girlsProductClass(request):
    if (request.method == "POST"):
        product_unique_id = random.randint(123456,9876543)
        product_name = request.POST.get('product_name')
        product_id = request.POST.get('product_id')
        product_category = request.POST.get('product_ctg')

        if(product_category==""):
            ctg_id = None
        else:
            ctg_id = girlCategoryTable.objects.get(category=product_category)

        product_brand = request.POST.get('product_brand')
        if(product_brand==""):
            bnd_id = None
        else:
            bnd_id = girlBrandTable.objects.get(brand=product_brand)
    
        product_tag = request.POST.get('product_tags')
        if(product_tag==""):
            tag_id = None
        else:
            tag_id = girlTagsTable.objects.get(tags=product_tag)

        product_size = request.POST.get('size')
        product_specification = request.POST.get('product_spec')
        product_color = request.POST.get('product_color')
        product_img = request.FILES.get('product_img')
        product_img_no = request.POST.get('product_img_no')
        product_opt_img = request.FILES.getlist('product_opt_img')
        womanProductClass = GirlProductTable(   product_unique_id=product_unique_id, 
                                                product_name=product_name, 
                                                product_id=product_id, 
                                                product_category=ctg_id, 
                                                product_brand=bnd_id, 
                                                product_tag=tag_id, 
                                                product_size=product_size, 
                                                product_specification=product_specification,  
                                                product_color=product_color, 
                                                product_img=product_img, 
                                                product_img_no=product_img_no, 
                                                date=datetime.today())
        womanProductClass.save()

        wp = GirlProductTable.objects.get(product_unique_id = product_unique_id)
        for f in product_opt_img:
            womanProductClass = ImagesForGirlProduct(product_unique_id=product_unique_id,product_opt_img=f,woman_product_id=wp)
            womanProductClass.save()
        
        response_data={
            'title' : 'Product added successfuly'
        }

        girls_update_all_item(product_category,product_brand,product_tag)
        return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')



def girls_update_all_item(ctg,bnd,tag):
    if (ctg!=''):
        ctg = girlCategoryTable.objects.get(category = ctg)
        category_item_no = GirlProductTable.objects.filter(product_category = ctg).count()
        girlCategoryTable.objects.filter(category = ctg).update(category_item_no = category_item_no)
    
    if (bnd!=''):
        bnd = girlBrandTable.objects.get(brand = bnd)
        brand_item_no = GirlProductTable.objects.filter(product_brand = bnd).count()
        girlBrandTable.objects.filter(brand = bnd).update(brand_item_no = brand_item_no)
    
    if (tag!=''):
        tag = girlTagsTable.objects.get(tags = tag)
        tags_no_item = GirlProductTable.objects.filter(product_tag = tag).count()
        girlTagsTable.objects.filter(tags = tag).update(tags_no_item = tags_no_item)





#<---------------------------------------------Admin Girls Zone End---------------------------------------->

#<---------------------------------------------Admin Boys Zone End----------------------------------------->

def admin_boys(request):
    if request.user.is_authenticated:
        category_data = boyCategoryTable.objects.all()
        ctg_no = boyCategoryTable.objects.count()

        brand_data = boyBrandTable.objects.all()
        bnd_no = boyBrandTable.objects.count()

        tags_data = boyTagsTable.objects.all()
        tag_no = boyTagsTable.objects.count()

        woman_data = BoyProductTable.objects.all()
        woman_no = BoyProductTable.objects.count()

        images_data = ImagesForBoyProduct.objects.all()
        
        return render(request,'admin2/boykidzone.html',{    'category_data':category_data, 
                                                            'brand_data':brand_data, 
                                                            'tags_data':tags_data, 
                                                            'woman_data':woman_data, 
                                                            'images_data':images_data, 
                                                            'ctg_no':ctg_no, 
                                                            'bnd_no':bnd_no,
                                                            'tag_no':tag_no,
                                                            'woman_no':woman_no })	
    else:
        return redirect('my-adminpage')

def boys_categoryClass(request):
    if (request.method == "POST"):
        category_name = request.POST.get('category')
        category_item_no = 0
        categoryClass = boyCategoryTable(category=category_name,category_item_no=category_item_no, date=datetime.today())
        categoryClass.save()
        response_data={
            'title' : 'Category added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return HttpResponseRedirect('/admin/boys')

def boys_brandClass(request):
    if (request.method == "POST"):
        brand_name = request.POST.get('brand')
        brand_item_no = 0
        brand_img = request.FILES.get('brand_img')
        brandClass = boyBrandTable(brand=brand_name, brand_item_no=brand_item_no, brand_img=brand_img, date=datetime.today())
        brandClass.save()
        response_data={
            'title' : 'Brand added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return HttpResponseRedirect('/admin/boys')

def boys_tagsClass(request):
    if (request.method == "POST"):
        tags_name = request.POST.get('tags')
        tags_no_item = 0
        tagsClass = boyTagsTable(tags=tags_name, tags_no_item=tags_no_item, date=datetime.today())
        tagsClass.save()
        response_data={
            'title' : 'Tags added successfuly'
        }
        return JsonResponse(response_data, safe=False)

    return HttpResponseRedirect('/admin/boys')

def boysProductClass(request):
    if (request.method == "POST"):
        product_unique_id = random.randint(123456,9876543)
        product_name = request.POST.get('product_name')
        product_id = request.POST.get('product_id')
        product_category = request.POST.get('product_ctg')

        if(product_category==""):
            ctg_id = None
        else:
            ctg_id = boyCategoryTable.objects.get(category=product_category)

        product_brand = request.POST.get('product_brand')
        if(product_brand==""):
            bnd_id = None
        else:
            bnd_id = boyBrandTable.objects.get(brand=product_brand)
    
        product_tag = request.POST.get('product_tags')
        if(product_tag==""):
            tag_id = None
        else:
            tag_id = boyTagsTable.objects.get(tags=product_tag)

        product_size = request.POST.get('size')
        product_specification = request.POST.get('product_spec')
        product_color = request.POST.get('product_color')
        product_img = request.FILES.get('product_img')
        product_img_no = request.POST.get('product_img_no')
        product_opt_img = request.FILES.getlist('product_opt_img')
        womanProductClass = BoyProductTable(    product_unique_id=product_unique_id, 
                                                product_name=product_name, 
                                                product_id=product_id, 
                                                product_category=ctg_id, 
                                                product_brand=bnd_id, 
                                                product_tag=tag_id, 
                                                product_size=product_size, 
                                                product_specification=product_specification,  
                                                product_color=product_color, 
                                                product_img=product_img, 
                                                product_img_no=product_img_no, 
                                                date=datetime.today())
        womanProductClass.save()

        wp = BoyProductTable.objects.get(product_unique_id = product_unique_id)
        for f in product_opt_img:
            womanProductClass = ImagesForBoyProduct(product_unique_id=product_unique_id,product_opt_img=f,man_product_id=wp)
            womanProductClass.save()
        
        response_data={
            'title' : 'Product added successfuly'
        }

        boys_update_all_item(product_category,product_brand,product_tag)
        return JsonResponse(response_data, safe=False)

    return HttpResponseRedirect('/admin/boys')


def boys_update_all_item(ctg,bnd,tag):
    if (ctg!=''):
        ctg = boyCategoryTable.objects.get(category = ctg)
        category_item_no = BoyProductTable.objects.filter(product_category = ctg).count()
        boyCategoryTable.objects.filter(category = ctg).update(category_item_no = category_item_no)
    
    if (bnd!=''):
        bnd = boyBrandTable.objects.get(brand = bnd)
        brand_item_no = BoyProductTable.objects.filter(product_brand = bnd).count()
        boyBrandTable.objects.filter(brand = bnd).update(brand_item_no = brand_item_no)
    
    if (tag!=''):
        tag = boyTagsTable.objects.get(tags = tag)
        tags_no_item = BoyProductTable.objects.filter(product_tag = tag).count()
        boyTagsTable.objects.filter(tags = tag).update(tags_no_item = tags_no_item)






#<---------------------------------------------Admin Boys Zone End----------------------------------------->

#<---------------------------------------------Admin Blog Start-------------------------------------------->
def blog(request):
    if request.user.is_authenticated:
        blog_data = BlogPost.objects.all()
        blog_no = BlogPost.objects.count()

        return render(request,'admin2/blog.html',{'blog_data':blog_data,'blog_no':blog_no})
    return redirect('my-adminpage')

def startblog(request):
    if request.user.is_authenticated:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")+str(random.randint(10,100))
        post_id = str(current_time)
        title = "(Untitled)"
        content = ""
        simple_post = ""
        status = 0
        post_url = "untitled-"+post_id

        editblog = BlogPost(post_id = post_id,title = title,content = content,simple_post = simple_post,status = status,post_url = post_url)
        editblog.save()
        return redirect("/my-adminpage/edit-blog/"+post_id)
    return redirect('my-adminpage')
    

def editblog(request,id):
    if request.user.is_authenticated:
        if BlogPost.objects.filter(post_id = id).exists():
            post = BlogPost.objects.get(post_id = id)
            return render(request,"Hillman Blog/editblog.html",{'post':post,'id':id})
    return redirect('my-adminpage')
    

def uploadblog(request):
    if request.user.is_authenticated:
        if (request.method == "POST"):
            id = request.POST.get('id')
            title = request.POST.get('title')
            content = request.POST.get('content')
            simple_post = request.POST.get('simple_post')
            status = request.POST.get('status')
            thumbnail_img = request.FILES.get('thumbnail_img')
            post = BlogPost.objects.get(post_id = id)
            if(title!=''):
                post_url = title.replace(' ', '-')
            else:
                post_url = "untitled-"+id

            
            uploadblog = BlogPost.objects.filter(post_id = id).update(post_id = id,title = title,content = content,simple_post = simple_post,status = status,thumbnail_img = thumbnail_img,post_url = post_url)

            response_data={
                'title' : 'Updated'
            }
            return JsonResponse(response_data, safe=False)
    return redirect('my-adminpage')
    

def finaluploadblog(request):
    if request.user.is_authenticated:
        if (request.method == "POST"):
            id = request.POST.get('id')
            title = request.POST.get('title')
            content = request.POST.get('content')
            simple_post = request.POST.get('simple_post')
            status = request.POST.get('status')
            thumbnail_img = request.FILES.get('thumbnail_img')

            if(title!=''):
                post_url = title.replace(' ', '-')
            else:
                post_url = "untitled-"+id

            finaluploadblog = BlogPost.objects.get(post_id = id)
            finaluploadblog.delete()

            finaluploadblog = BlogPost(post_id = id,title = title,content = content,simple_post = simple_post,status = status,thumbnail_img = thumbnail_img,post_url = post_url)
            finaluploadblog.save()

            response_data={
                'title' : 'Updated'
            }
            return JsonResponse(response_data, safe=False)
    return redirect('my-adminpage')


def edit_req_blog(request):
    if request.user.is_authenticated:
        if (request.method == "POST"):
            id = request.POST.get('id')
            if BlogPost.objects.filter(post_id = id).exists():
                response_data={
                'status' : 1,
                'title':'Blog exist'
                }
                return JsonResponse(response_data, safe=False)
            else:
                response_data={
                'status' : 0,
                'title':'Blog not exist'
                }
                return JsonResponse(response_data, safe=False)

    return redirect('my-adminpage')


            


    
#<---------------------------------------------Admin Blog End-------------------------------------------->