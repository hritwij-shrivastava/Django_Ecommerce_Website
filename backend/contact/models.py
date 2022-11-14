from django.db import models

# Create your models here.

class contactTable(models.Model):
    background_img = models.ImageField(upload_to="pages")
    address = models.CharField(max_length=122)
    phoneNo = models.CharField(max_length=122)
    email_id = models.CharField(max_length=122)
    workingHour1 = models.CharField(max_length=122)
    workingHour2 = models.CharField(max_length=122)
    facebook_url = models.CharField(max_length=122)
    twitter_url = models.CharField(max_length=122)
    insta_url = models.CharField(max_length=122)
    linkedin_url = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)


class userMessage(models.Model):
    user_name = models.CharField(max_length=122)
    user_email = models.CharField(max_length=122)
    user_msz = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class footerAbout(models.Model):
    title = models.CharField(max_length=122)
    url = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class footerCategories(models.Model):
    title = models.CharField(max_length=122)
    url = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class footerUsefulLink(models.Model):
    title = models.CharField(max_length=122)
    url = models.CharField(max_length=122)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title