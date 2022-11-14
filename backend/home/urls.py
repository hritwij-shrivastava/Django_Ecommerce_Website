from django.contrib import admin
from django.urls import path,include, re_path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='index'),

]