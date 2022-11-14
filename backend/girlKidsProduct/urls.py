from django.contrib import admin
from django.urls import path,include, re_path
from girlKidsProduct import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [

    path("girlsproduct",views.girls_product,name='girls_product'),
    path('girlsproduct-description',RedirectView.as_view(url='/girls-product')),
    path('girlsproduct-description/<id>',views.girls_product_url_generator,name='girls_product_url_detail'),
    path('girlsproduct-description/<id>/<url>',views.girls_productDetail,name='girls_product_list_detail'),
    path("girls-ajax-pagination",views.girls_ajax_pagination,name='girls_ajax_pagination'),
    path("girls-ajax-color-spliter",views.girls_ajax_color_spliter,name='girls_ajax-color-spliter'),

]