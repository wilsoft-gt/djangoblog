from django.db import models

# Create your models here.
class blogposts(models.Model):
    post_title = models.CharField(max_length=100)
    post_image_header = models.CharField(max_length=200)
    post_body = models.TextField()
    post_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.post_title

class images(models.Model):
    imagefile = models.ImageField(upload_to="blog/images")
    