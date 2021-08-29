from django.db import models

# Create your models here.
class CoinbaseKeys(models.Model):
    key = models.CharField(max_length=32, unique=True)
    passphrase = models.CharField(max_length=11, unique=True)
    secret = models.CharField(max_length=88, unique=True)

class Orders(models.Model):
    currency_name = models.CharField(max_length=10)
    funds = models.FloatField()
    schedule = models.IntegerField(max_length=10)

