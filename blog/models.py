from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blogposts(models.Model):
    post_title = models.CharField(max_length=100)
    post_image_header = models.CharField(max_length=200)
    post_body = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    post_views = models.IntegerField(default=0)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_like = models.IntegerField(default=0)
    post_count_comments = models.IntegerField(default=0)
    #post_shares = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

class images(models.Model):
    imagefile = models.ImageField(upload_to="blog/images")
    imagedate = models.DateTimeField(auto_now=True)
    imageuser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
class comment(models.Model):
    comment_name = models.CharField(max_length=42)
    comment_email = models.EmailField(max_length=75)
    comment_comment = models.TextField()
    comment_date = models.DateTimeField(auto_now=True)
    comment_post = models.ForeignKey(blogposts, on_delete=models.CASCADE, null=True)
    