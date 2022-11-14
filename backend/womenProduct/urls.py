from django.contrib import admin
from django.urls import path,include, re_path
from womenProduct import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [

    path("womenproduct",views.product,name='product'),
    path('womenproduct-description',RedirectView.as_view(url='/product')),
    path('womenproduct-description/<id>',views.product_url_generator,name='product-url-detail'),
    path('womenproduct-description/<id>/<url>',views.productDetail,name='product-list-detail'),
    path("ajax-pagination",views.ajax_pagination,name='ajax_pagination'),
    path("ajax-color-spliter",views.ajax_color_spliter,name='ajax-color-spliter'),

]