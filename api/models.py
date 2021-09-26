from django.db import models
from django.utils.translation import activate

class CoinbaseKeys(models.Model):
    nickname = models.CharField(max_length=100)
    api_key = models.CharField(max_length=32, unique=True)
    api_passphrase = models.CharField(max_length=11, unique=True)
    api_secret = models.CharField(max_length=88, unique=True)

    def __str__(self):
        return self.nickname


class Orders(models.Model):
    DAILY = 'D'
    WEEKLY = 'W'
    MONTHLY = 'M'
    FREQUENCIES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
    )
    currency_name = models.CharField(max_length=10)
    funds = models.FloatField()
    frequency = models.CharField(
        choices=FREQUENCIES, max_length=1, default=DAILY)
    coinbase_account = models.ForeignKey(
        CoinbaseKeys, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
