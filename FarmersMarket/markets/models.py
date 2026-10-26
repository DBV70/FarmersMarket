from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from FarmersMarket.producers.models import Producer

class MarketDay(models.Model):
    class MarketType(models.TextChoices):
        FOOD_MARKET = 'FOOD_MARKET', 'Food Market'
        RETAIL_MARKET = 'RETAIL_MARKET', 'Retail Market'
        FARM_MARKET = 'FARM_MARKET', 'Farm Market'
        FISHING_MARKET = 'FISHING_MARKET', 'Fishing Market'
        OTHERS = 'OTHERS', 'Others'

    date = models.DateField()
    location = models.CharField(max_length=100)
    market_type = models.CharField(max_length=50, choices=MarketType.choices)
    description = models.TextField()
    market_open = models.DateTimeField(validators=[MinValueValidator('08:00'), MaxValueValidator('12:00')])
    market_close = models.DateTimeField(validators=[MinValueValidator(market_open), MaxValueValidator('19:00')])
    producers = models.ManyToManyField(Producer, related_name='market_days')
