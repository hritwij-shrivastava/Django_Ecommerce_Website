from django.db import models

# Create your models here.

#Table For first carousel Slider Image

class SliderImages(models.Model):
    sliderImage = models.ImageField(upload_to="pages")
    date = models.DateField(auto_now_add=True)

#Table For header text below to carousel

class HeaderText(models.Model):
    title = models.CharField(max_length=122)
    desc = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

#Table to store all the ids of product to be displayed on index.html
 
class ProductID(models.Model):
    pid = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pid

#table for image that sliding upwards

class UpSliderImages(models.Model):
    upsliderImage = models.ImageField(upload_to="pages")
    date = models.DateField(auto_now_add=True)

#Table for storing logo images on index
 
class LogoImages(models.Model):
    logoImage = models.ImageField(upload_to="pages")
    date = models.DateField(auto_now_add=True)


#Table for storing url to be displayed on index.html

class AdVideo(models.Model):
    url = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)


#Table for all footer image

class InstaImages(models.Model):
    instaImage = models.ImageField(upload_to="pages")
    date = models.DateField(auto_now_add=True)