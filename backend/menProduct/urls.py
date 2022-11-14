from django.contrib import admin
from django.urls import path,include, re_path
from menProduct import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [

    path("menproduct",views.men_product,name='m_product'),
    path('menproduct-description',RedirectView.as_view(url='/m_product')),
    path('menproduct-description/<id>',views.men_product_url_generator,name='m_product-url-detail'),
    path('menproduct-description/<id>/<url>',views.men_productDetail,name='m_product-list-detail'),
    path("m-ajax-pagination",views.men_ajax_pagination,name='m_ajax_pagination'),
    path("m-ajax-color-spliter",views.men_ajax_color_spliter,name='m_ajax-color-spliter'),

]