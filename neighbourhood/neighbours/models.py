from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey('auth.User',null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,name):
        cls.objects.filter(name=name).delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Business(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    location =models.CharField(max_length=100)
    phone = models.IntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
class EmergencyService(models.Model):
    type = models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    description = models.TextField()
    location =models.CharField(max_length=100)
    phone = models.IntegerField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    post = models.TextField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)

    def __str__(self):
        return self.title