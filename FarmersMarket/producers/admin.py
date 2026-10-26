from django.contrib import admin
from FarmersMarket.producers.models import Producer

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    list_filter = ('country',)
    search_fields = ('name',)