from django.db import models

# Create your models here.


class Clothes(models.Model):
    img = models.ImageField(upload_to='static/assets')
    title = models.CharField(max_length=100)
    price = models.IntegerField()

class Shoes(models.Model):
    img = models.ImageField(upload_to='static/assets')
    title = models.CharField(max_length=100)
    price = models.IntegerField()

class Watch(models.Model):
    img = models.ImageField(upload_to='static/assets')
    title = models.CharField(max_length=100)
    price = models.IntegerField()

class Cap(models.Model):
    img = models.ImageField(upload_to='static/assets')
    title = models.CharField(max_length=100)
    price = models.IntegerField()