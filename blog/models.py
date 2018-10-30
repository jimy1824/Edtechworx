from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField
from about.models import Team

# Create your models here.

class BlogBanner(models.Model):
    heading =models.CharField(max_length=500)
    created_date =models.DateTimeField(auto_now=True)
    content= models.TextField()
    background_image = models.ImageField(upload_to='background_imgs/', blank=True)

    def __str__(self):
        return '%s %s' % (self.heading, self.content)

class BlogComments(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    comment= models.TextField()
    posting_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Blogs(models.Model):
    author = models.ForeignKey(Team ,on_delete=models.CASCADE )
    title = models.CharField(max_length=100)
    sub_title=models.CharField(max_length=500 ,blank=True)
    description = models.TextField()
    detail_description = RichTextField()
    posting_date = models.DateTimeField()
    header_image = models.ImageField(upload_to='header_image/')
    fb_link = models.CharField(max_length=500,blank=True)
    twiter_link = models.CharField(max_length=500, blank=True)
    comments=models.ManyToManyField(BlogComments )


    def __str__(self):
        return '%s %s' % (self.sub_title, self.title)






