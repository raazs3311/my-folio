from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=20, null=True)
    Email = models.EmailField(max_length=30, null=True)
    query = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Name

class Images(models.Model):
    img = models.FileField(upload_to='static')

    

class projectimg(models.Model):
    proimg = models.FileField(upload_to='static/image')

class resume(models.Model):
    res = models.FileField(upload_to= 'static/image')

class profile(models.Model):
    profile_img = models.FileField(upload_to= 'static/image')

