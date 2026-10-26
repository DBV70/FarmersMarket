import datetime
from django.core.exceptions import ValidationError
from django.db import models
from FarmersMarket.producers.models import Producer

class MarketDay(models.Model):
    OPEN_EARLIEST = datetime.time(8, 0)
    OPEN_LATEST = datetime.time(12, 0)
    CLOSE_LATEST = datetime.time(19, 0)

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
    market_open = models.TimeField()
    market_close = models.TimeField()
    producers = models.ManyToManyField(Producer, related_name='market_days')

    def clean(self):
        super().clean()
        errors = {}

        if self.market_open:
            if self.market_open < self.OPEN_EARLIEST or self.market_open > self.OPEN_LATEST:
                errors['market_open'] = f"Market open time must be between {self.OPEN_EARLIEST:%H:%M} and {self.OPEN_LATEST:%H:%M}."

        if self.market_close:
            if self.market_close > self.CLOSE_LATEST:
                errors['market_close'] = f"Market close time must be before {self.CLOSE_LATEST:%H:%M}."

        if self.market_open and self.market_close:
            if self.market_open >= self.market_close:
                errors['market_close'] = "Market open time must be before market close time."

        if  self.date and self._state.adding:
            if self.date < datetime.date.today():
                errors['date'] = "Market date must be today or in the future."

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.date} - {self.location} - {self.market_type}"
