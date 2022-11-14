from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blog.models import BlogPost
import random
from contact.models import contactTable, footerAbout, footerCategories, footerUsefulLink

# Create your views here.


def viewblog(request):
    blog_post = BlogPost.objects.filter(status=1)
    num_latest_post = BlogPost.objects.filter(status=1).count()
        
    contact_table = contactTable.objects.all()
    footer_about = footerAbout.objects.all()
    footer_categories = footerCategories.objects.all()
    footer_usefullink = footerUsefulLink.objects.all()

    if num_latest_post < 3:
        status = 0
        return render(request,"allblog.html",{  'blog_post':blog_post,
                                                'status':status,
                                                
                                                'contact_table':contact_table,
                                                'footer_about':footer_about,
                                                'footer_categories':footer_categories,
                                                'footer_usefullink':footer_usefullink,})
    else:      
        latest_1 = BlogPost.objects.filter(status=1).order_by('-id')[0]
        five_latest_1 = latest_1.simple_post.split()[:5] 

        latest_2 = BlogPost.objects.filter(status=1).order_by('-id')[1]
        five_latest_2 = latest_2.simple_post.split()[:5] 

        latest_3 = BlogPost.objects.filter(status=1).order_by('-id')[2]
        five_latest_3 = latest_3.simple_post.split()[:5] 

        status = 1


        return render(request,"allblog.html",{  'blog_post':blog_post,
                                                'status':status,
                                                'latest_1':latest_1,
                                                'latest_2':latest_2,
                                                'latest_3':latest_3,
                                                'five_latest_1':five_latest_1,
                                                'five_latest_2':five_latest_2,
                                                'five_latest_3':five_latest_3,
                                                
                                                'contact_table':contact_table,
                                                'footer_about':footer_about,
                                                'footer_categories':footer_categories,
                                                'footer_usefullink':footer_usefullink,})

def redirectblog(request,id):
    if BlogPost.objects.filter(post_id = id).exists():
        post = BlogPost.objects.get(post_id = id)
        url = post.post_url
        return redirect("/blog/"+id+"/"+url)
    
    return redirect("/blog")

def finalblog(request,id,url):
    if BlogPost.objects.filter(post_id = id).exists():
        post = BlogPost.objects.get(post_id = id)

        contact_table = contactTable.objects.all()
        footer_about = footerAbout.objects.all()
        footer_categories = footerCategories.objects.all()
        footer_usefullink = footerUsefulLink.objects.all()
        return render(request,"Hillman Blog/viewblog.html",{'post':post,
                                                            'contact_table':contact_table,
                                                            'footer_about':footer_about,
                                                            'footer_categories':footer_categories,
                                                            'footer_usefullink':footer_usefullink,})
        
    return redirect("/blog")