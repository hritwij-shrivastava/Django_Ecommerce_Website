from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from about.models import aboutSliderImages, aboutHeaderText, companyData, vision, leadership
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink

def index(request):
        about_slider_images = aboutSliderImages.objects.all()
        about_slider_images_count = aboutSliderImages.objects.count()

        about_header_text = aboutHeaderText.objects.all()

        company_data = companyData.objects.all()

        vision_data = vision.objects.all()

        leadership_data = leadership.objects.all()

        contact_table = contactTable.objects.all()
        footer_about = footerAbout.objects.all()
        footer_categories = footerCategories.objects.all()
        footer_usefullink = footerUsefulLink.objects.all()

        return render(request,'about.html',{'about_slider_images':about_slider_images,
                                            'range': range(0,about_slider_images_count),
                                            'about_header_text':about_header_text,
                                            'company_data':company_data,
                                            'vision_data':vision_data,
                                            'leadership_data':leadership_data,
                                            
                                            'contact_table':contact_table,
                                            'footer_about':footer_about,
                                            'footer_categories':footer_categories,
                                            'footer_usefullink':footer_usefullink,})