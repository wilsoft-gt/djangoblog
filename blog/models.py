from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blogposts(models.Model):
    post_title = models.CharField(max_length=100)
    post_image_header = models.CharField(max_length=200)
    post_body = models.TextField()
    post_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_views = models.IntegerField(default=0)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_like = models.IntegerField(default=0)
    post_count_comments = models.IntegerField(default=0)
    #post_shares = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

class images(models.Model):
    imagefile = models.ImageField(upload_to="blog/images")
    imagedate = models.DateTimeField(auto_now=False, auto_now_add=True)
    imageuser = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.imagefile.name
    
class comment(models.Model):
    comment_name = models.CharField(max_length=42)
    comment_email = models.EmailField(max_length=75)
    comment_comment = models.TextField()
    comment_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    comment_post = models.ForeignKey(blogposts, on_delete=models.CASCADE, null=True)
    comment_moderated = models.BooleanField(default=False)
    def __str__(self):
        return self.comment_name
    
class adminExtraField(models.Model):
    adminFields_image = models.ImageField(upload_to="blog/adminimages")
    adminFields_bio = models.TextField()
    adminFields_quote = models.TextField()
    adminFields_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.adminFields_image.name