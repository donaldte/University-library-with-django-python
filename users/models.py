
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

import os

def rename_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = "photo_profile/{}.{}".format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_not_verified = models.BooleanField(default=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=100)
    
    
    NAHPI = 'NAHPI'
    FSCH = 'FSCH'
    HCIM = 'HCIM'
    FACULTY = 'FACULTY'
    ENS = 'ENS'
    ENSET = 'ENSET'

    SCHOOL = [
        ( NAHPI, 'NAHPI'),( FSCH , 'FSCH'), ( HCIM, 'HCIM'),( FACULTY ,'FACULTY'),
        ( ENS, 'ENS'), (ENSET, 'ENSET')
    ]

    school = models.CharField(max_length=100, choices=SCHOOL, default='NAHPI')
    department = models.CharField(max_length=100)
    l1='1'
    l2='2'
    l3='3'
    l4='4'
    l5='5'
    l6='6'
    l7='7'
    level = [
        (l1,'1'),
        (l2,'2'),
        (l3,'3'),
        (l4,'4'),
        (l5,'5'),
        (l6,'6'),
        (l7,'7')

    ]
    level =  models.CharField(max_length=100, choices=level, default='1')
    picture = models.ImageField(upload_to=rename_image, blank=True)


    def __str__(self):
        return self.user.username

    
    


class Ecategory(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name


class Ebooks(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Ecategory, on_delete=models.CASCADE, blank=True, null=True)
    pdf = models.FileField(upload_to='pdf', blank=True)
    cover = models.ImageField(upload_to='ecover', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = ('Ebook')
        verbose_name_plural = ('Ebooks')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        self.pdf.delete()
        super().delete(*args, **kwargs)        

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Ecategory, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_by = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='cover', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = ('Book')
        verbose_name_plural = ('Books')


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)    


class Chats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = ("Chat")
        verbose_name_plural = ("Chats")

    def __str__(self):
        return self.message

class SendFeedback(models.Model):
    feedback = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.feedback   

    def get_absolute_url(self):
        return reverse("feedback_delete", kwargs={"pk": self.pk})


class CommandBook(models.Model):
    name = models.ForeignKey(Books, on_delete=models.CASCADE)
    comand_date = models.DateTimeField(auto_now_add=True)
    student_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)
    class Meta:
        ordering = ['-comand_date']

    def __str__(self):
        return self.name.title


    



