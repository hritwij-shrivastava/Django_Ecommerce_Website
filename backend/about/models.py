from django.db import models

# Create your models here.

class aboutSliderImages(models.Model):
    sliderImage = models.ImageField(upload_to="pages")
    date = models.DateField(auto_now_add=True)


class aboutHeaderText(models.Model):
    title = models.CharField(max_length=122)
    desc = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class companyData(models.Model):
    data1 = models.CharField(max_length=122)
    title_data1 = models.CharField(max_length=122)
    data2 = models.CharField(max_length=122)
    title_data2 = models.CharField(max_length=122)
    data3 = models.CharField(max_length=122)
    title_data3 = models.CharField(max_length=122)
    data4 = models.CharField(max_length=122)
    title_data4 = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

class vision(models.Model):
    visionImage = models.ImageField(upload_to="pages")
    vision_desc = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

class leadership(models.Model):
    leaderImage = models.ImageField(upload_to="pages")
    leader_name = models.CharField(max_length=122)
    leader_designation = models.CharField(max_length=122)
    leader_desc = models.CharField(max_length=122)
    leader_social_media = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.leader_name