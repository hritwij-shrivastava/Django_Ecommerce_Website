from django.contrib import admin
from django.urls import path,include, re_path
from adminpanel import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path("my-adminpage",views.my_admin_page,name='my-adminpage'),
    path("my-adminpagelogin",views.my_admin_pagelogin,name='my-adminpagelogin'),
    path("my-adminpagelogout",views.my_admin_pagelogout,name='my-adminpagelogout'),


    path("my-adminpage/home",views.admin_home,name='admin-home'),
    path("slider-submit",views.updateSlider,name='slider-submit'),
    path("header-submit",views.headerText,name='headr-submit'),
    path("product-id-submit",views.productID,name='product-id-submit'),
    path("upslider-submit",views.updateUpSlider,name='upslider-submit'),
    path("logo-home-submit",views.logoImage,name='logo-home-submit'),
    path("ad-video-submit",views.ad_Video,name='ad-video-submit'),
    path("insta-pic-submit",views.insta_Image,name='insta-pic-submit'),


    path("my-adminpage/about",views.admin_about,name='admin-about'),
    path("about-slider-submit",views.about_slider,name='about-slider-submit'),
    path("about-header-submit",views.about_header,name='about-header-submit'),
    path("about-companydata-submit",views.about_companydata,name='about-companydata-submit'),
    path("about-vision-submit",views.about_vision,name='about-vision-submit'),
    path("about-leadership-submit",views.about_leadership,name='about-leadership-submit'),

    
    path("my-adminpage/contact",views.admin_contact,name='admin-contact'),
    path("contact-info-submit",views.contact_info,name='contact-info-submit'),
    path("footer-about-submit",views.footer_about,name='footer-about-submit'),
    path("footer-category-submit",views.footer_category,name='footer-category-submit'),
    path("footer-useful-submit",views.footer_useful,name='footer-useful-submit'),


    path("my-adminpage/womenzone",views.admin_women,name='admin_woman'),
    path("category-submit",views.categoryClass,name='category_submit'),
    path("brand-submit",views.brandClass,name='brand_submit'),
    path("tags-submit",views.tagsClass,name='tags_submit'),
    path("product-submit",views.womanProductClass,name='product_submit'),


    path("my-adminpage/menzone",views.admin_men,name='admin_man'),
    path("m-category-submit",views.men_categoryClass,name='m_category_submit'),
    path("m-brand-submit",views.men_brandClass,name='m_brand_submit'),
    path("m-tags-submit",views.men_tagsClass,name='m_tags_submit'),
    path("m-product-submit",views.MenProductClass,name='m_product_submit'),


    path("my-adminpage/girlszone",views.admin_girls,name='admin_girls'),
    path("girls-category-submit",views.girls_categoryClass,name='girls_category_submit'),
    path("girls-brand-submit",views.girls_brandClass,name='girls_brand_submit'),
    path("girls-tags-submit",views.girls_tagsClass,name='girls_tags_submit'),
    path("girls-product-submit",views.girlsProductClass,name='girls_product_submit'),


    path("my-adminpage/boyszone",views.admin_boys,name='admin_boy'),
    path("boys-m-category-submit",views.boys_categoryClass,name='boys_m_category_submit'),
    path("boys-m-brand-submit",views.boys_brandClass,name='boys_m_brand_submit'),
    path("boys-m-tags-submit",views.boys_tagsClass,name='boys_m_tags_submit'),
    path("boys-m-product-submit",views.boysProductClass,name='boys_m_product_submit'),


    path("my-adminpage/blog",views.blog,name='blog'),
    path("my-adminpage/edit-blog",views.startblog,name='start-editblog'),
    path("my-adminpage/edit-blog/<id>",views.editblog,name='editblog'),
    path("my-adminpage/edit/upload",views.uploadblog,name='upload'),
    path("my-adminpage/edit/finalupload",views.finaluploadblog,name='finalupload'),
    path("my-adminpage/edit-blog-request",views.edit_req_blog,name='edit_req'),

]