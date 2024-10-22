from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.topic_name
class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    url=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Accessrecord(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField()
    location=models.CharField(max_length=100,default='Bangalore')
    def __str__(self):
        return self.name
    