from django.core.validators import MinValueValidator
from django.db import models
from FarmersMarket.producers.models import Producer

class Product(models.Model):
    class ProductCategory(models.TextChoices):
        FRUITS = 'FRUITS', 'Fruits'
        VEGETABLES = 'VEGETABLES', 'Vegetables'
        BERRIES = 'BERRIES', 'Berries'
        HERBS = 'HERBS', 'Herbs'
        SPICES = 'SPICES', 'Spices'
        FLOURS = 'FLOURS', 'Flours'
        MEAT = 'MEAT', 'Meat'
        DAIRY = 'DAIRY', 'Dairy'
        FISH = 'FISH', 'Fish'
        SEAFOOD = 'SEAFOOD', 'Seafood'
        BAKERY = 'BAKERY', 'Bakery'
        BEVERAGES = 'BEVERAGES', 'Beverages'
        SNACKS = 'SNACKS', 'Snacks'
        OTHERS = 'OTHERS', 'Others'

    class UnitChoices(models.TextChoices):
        KG = 'KG', 'Kilograms'
        L = 'L', 'Liters'
        G = 'G', 'Grams'
        ML = 'ML', 'Milliliters'
        PCS = 'PCS', 'Pieces'

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=ProductCategory.choices)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=10, choices=UnitChoices.choices, default=UnitChoices.PCS)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    image = models.ImageField(upload_to='media/products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
