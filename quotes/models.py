import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Source(models.Model):
    TYPE_CHOICES = [
        ('1' , "Tweet"),
        ('2' , 'Article'),
        ('3' , "Podcast"),
        ('4' , "Not Specfied"),
    ]
    type_text = models.CharField(max_length = 20, choices = TYPE_CHOICES, default='4')
    url = models.URLField(max_length=200)
    title_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published at')

    def __str__(self):
        return self.title_text

class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    author_text = models.CharField(max_length=200)
    CHOICES = [
        ('-1' , "Negative"),
        ('1' , "Positive"),
        ('0' , "Neutral"),
    ]
    sentiment = models.CharField(max_length = 8, choices = CHOICES, default='0')
    create_date = models.DateTimeField('created at')
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text




