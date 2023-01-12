from django.db import models

# Create your models here.


class News(models.Model):
    body = models.CharField(max_length = 100 , default = "Not news yet" , blank = False)

class Updates(models.Model):
    update = models.CharField(max_length = 100 , default = "Not updates yet" , blank = False)

class Service(models.Model):
    service_name = models.CharField(max_length = 50 , blank = False , default = "Not service available yet")
    service_price = models.CharField(max_length = 50 , blank = False , default = "Not service available yet")
    options = models.TextField(default = "Not service available yet")