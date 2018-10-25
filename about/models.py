
from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    designation=models.CharField(max_length=500)
    qulification = models.TextField()
    interest= models.TextField()
    aims = models.TextField()
    other = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class CompanyAbouts(models.Model):
    heading = models.CharField(max_length=500)
    description = models.TextField()
    company_profile = models.ImageField(upload_to='company_profile/')


    def __str__(self):
        return '%s' % (self.heading)
