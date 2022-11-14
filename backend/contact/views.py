from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from contact.models import contactTable, userMessage, footerAbout, footerCategories, footerUsefulLink

# Create your views here.
def index(request):
    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()

    return render(request,'contact.html',{  'contact_table':contact_table,
                                            'footer_about':footer_about,
                                            'footer_categories':footer_categories,
                                            'footer_usefullink':footer_usefullink,})    

def form_contact(request):
    if request.method == 'POST':
        status= request.POST.get('status')
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')

        if(status == 1 and name!='',email!='',phone!=''):
            response_data={
                'status' : 1,
                'url': 'https://script.google.com/macros/s/AKfycbxCbEqBSizIC1YFyZHWHB4qfCC6vheSv_KWzvaZHj3_qofYLKEBcV4Ab7YF2Uhv9kBnSw/exec',
                'title' : 'Query sent successfullly'
            }
            return JsonResponse(response_data, safe=False)
        else:
            response_data={
            'title' : 'Please Fill All details'
            }
            return JsonResponse(response_data, safe=False)
