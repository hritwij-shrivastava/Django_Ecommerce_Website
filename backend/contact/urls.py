from django.contrib import admin
from django.urls import path,include, re_path
from contact import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("contacts",views.index,name='contact'),
]