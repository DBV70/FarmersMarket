from django.contrib import admin
from FarmersMarket.markets.models import MarketDay

@admin.register(MarketDay)
class MarketDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'market_type',)
    list_filter = ('date',)
    search_fields = ('location',)
