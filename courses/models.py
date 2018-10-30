from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
VIDEO = 'video'
IMAGE = 'image'
YOUTUBE = 'youtube'
MATERIAL_CHOICES = (

        (VIDEO, 'VIDEO'),
        (IMAGE, 'IMAGE'),
        (YOUTUBE, 'YOUTUBE'),

    )

class CourseComments(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    comment= models.TextField()
    posting_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Course(models.Model):
    title = models.CharField(max_length=500)
    description=models.TextField()
    trainer_name=models.CharField(max_length=500)
    course_fee=models.IntegerField()
    shedule=models.CharField(max_length=500)
    available_seats=models.IntegerField()
    objectives= models.TextField()
    eligibility = models.TextField()
    courseoutline = RichTextField()
    background_image = models.ImageField(upload_to='courses_imgs/')
    material_type = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default=IMAGE)
    material = models.FileField(upload_to='helpingmatrial/', blank=True)
    url = models.CharField(max_length=150, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(CourseComments)

    def __str__(self):
        return '%s %s' % (self.title, self.created_date)



class CoursesBanner(models.Model):
    heading =models.CharField(max_length=500)
    created_date =models.DateTimeField(auto_now=True)
    content= models.TextField()
    background_image = models.ImageField(upload_to='background_imgs/', blank=True)

    def __str__(self):
        return '%s %s' % (self.heading, self.content)