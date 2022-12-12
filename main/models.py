from django.db import models
from .youtube import getVideoInfo
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

def validate_file(value):
    value= str(value)
    if value.endswith(".pdf") != True and value.endswith(".doc") != True and value.endswith(".docx") != True: 
        raise ValidationError("Only PDF and Word Documents can be uploaded")
    else:
        return value

# Create your models here.

class LeadPastors(models.Model):
    fullname = models.CharField(max_length=30)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='LeadPastors')

    def __str__(self) -> str:
        return self.fullname


class BookLibrary(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    short_description = models.TextField(null=True, blank=True)
    cover_page = models.ImageField(upload_to='BookLibrary/CoverPage')
    pdf = models.FileField(upload_to='BookLIbrary/PDf', max_length=100, validators=[validate_file])

    
    def __str__(self) -> str:
        return self.title


class VideoMessage(models.Model):
    url = models.URLField(max_length=200)
    video_id = models.CharField(null=True, max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
       ordering = ['date_posted']

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        title, path = getVideoInfo(self.url)
        self.title = title
        self.video_id = path
        super().save()


class NewsLetter(models.Model):
    subject = models.CharField( max_length=50)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.body


class NewsLetterUsers(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class PrayerRequest(models.Model):
    firstname = models.CharField( verbose_name='First name',max_length=50)
    lastname = models.CharField(verbose_name='Last name' , max_length=50)
    email = models.EmailField( max_length=254)
    phone = PhoneNumberField()
    request = models.CharField(verbose_name='Prayer Request', max_length=2000)
    