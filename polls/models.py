import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    phoneNumber = PhoneNumberField()
    
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()   
   

    def __str__(self):
        return self.user.username
  
class Home(models.Model):
    text = models.TextField()
    picture = models.ImageField(upload_to = 'img', blank = True, null = True)


    def __str__(self):
        return self.text

class Clothes(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    picture = models.FileField(upload_to = 'img', blank = True, null = True)

class Customs(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    picture = models.ImageField(upload_to = 'img', blank = True, null = True)

class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    picture = models.ImageField(upload_to = 'img', blank = True, null = True)

    def __str__(self):
        return self.question       
 

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died',null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super(Author, self).save(*args, **kwargs)
