from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.urls import reverse


class Neighbourhood(models.Model):
    image = models.ImageField(upload_to='images/', default='noimage.png')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # new
        return reverse('hood-update', args=[str(self.id)])

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,name):
        cls.objects.filter(name=name).delete()

class UserManager(BaseUserManager):
    def create_user(self, email, username,firstname,county, estate, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not firstname:
            raise ValueError('Users must have a  first name')
        if not estate:
            raise ValueError('Users must enter a county name')
        if not county:
            raise ValueError('Users must enter an estate name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname = firstname,
            estate = estate,
            county = county
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,firstname,county, estate, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            firstname=firstname,
            estate=estate,
            county=county
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    estate = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='user')
    hood = models.ForeignKey(Neighbourhood, null=True, blank=True, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstname', 'county', 'estate']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Business(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    location =models.CharField(max_length=100)
    phone = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
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
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)

    def __str__(self):
        return self.title