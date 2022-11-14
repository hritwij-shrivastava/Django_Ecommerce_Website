from django.contrib import admin
from django.urls import path,include, re_path
from boyKidsProduct import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [

    path("boysproduct",views.boys_product,name='boys_m_product'),
    path('boysproduct-description',RedirectView.as_view(url='/boys_m_product')),
    path('boysproduct-description/<id>',views.boys_product_url_generator,name='boys_m_product-url-detail'),
    path('boysproduct-description/<id>/<url>',views.boys_productDetail,name='boys_m_product-list-detail'),
    path("boys-m-ajax-pagination",views.boys_ajax_pagination,name='boys_m_ajax_pagination'),
    path("boys-m-ajax-color-spliter",views.boys_ajax_color_spliter,name='boys_m_ajax-color-spliter'),

]