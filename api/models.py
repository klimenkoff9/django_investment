from django.db import models

# Create your models here.


class Store(models.Model):
    key = models.CharField(max_length=100, unique=True)
    passphrase = models.CharField(max_length=100, unique=True)
    secret = models.CharField(max_length=100, unique=True)

class Order(models.Model):
    product_id = models.CharField(max_length=10)
    funds = models.FloatField()
    side = models.CharField(max_length=10)

