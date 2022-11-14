from django.db import models

class BlogPost(models.Model):
    post_id = models.CharField(max_length=122)
    title = models.CharField(max_length=122)
    content = models.TextField(blank=True, null=True)
    simple_post = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=122)
    post_url = models.CharField(max_length=122)
    thumbnail_img = models.ImageField(upload_to="blog_contents",blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
            return self.title
