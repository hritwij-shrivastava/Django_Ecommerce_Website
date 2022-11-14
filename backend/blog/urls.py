from django.contrib import admin
from django.urls import path,include, re_path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [

    path("blog",views.viewblog,name='viewblog'),
    path("blog/<id>",views.redirectblog,name='redirectblog'),
    path("blog/<id>/<url>",views.finalblog,name='finalblog'),
] 