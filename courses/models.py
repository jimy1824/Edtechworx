from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=500)
    description=models.TextField()
    trainer_name=models.CharField(max_length=500)
    course_fee=models.IntegerField()
    shedule=models.CharField(max_length=500)
    available_seats=models.IntegerField()
    objectives= models.TextField()
    eligibility = models.TextField()
    courseoutline = models.TextField()
    background_image = models.ImageField(upload_to='courses_imgs/')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.title, self.created_date)
