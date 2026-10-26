from datetime import date, datetime, time, timedelta
from decimal import Decimal
import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from FarmersMarket.markets.models import MarketDay
from FarmersMarket.producers.models import Producer
from FarmersMarket.products.models import Product


class Command(BaseCommand):
    help = "Seed market data with meaningful records."

    def handle(self, *args, **options):
        random.seed(42)

        producer_blueprints = [
            ("Green Valley Farm", "12 Orchard Lane", "US", "Family-run farm focused on seasonal fruits and vegetables."),
            ("Sunny Creek Organics", "48 River Road", "US", "Certified organic producer with mixed crops."),
            ("North Ridge Dairy", "7 Meadow Street", "US", "Small-batch dairy with fresh milk and cheese."),
            ("Coastal Catch Cooperative", "102 Harbor Ave", "US", "Local fishers supplying fresh and smoked fish."),
            ("Maple Grove Apiary", "31 Bee Hill", "US", "Raw honey and bee products from local hives."),
            ("Stone Mill Bakers", "15 Baker Square", "US", "Artisan breads and baked goods made daily."),
            ("Oakwood Meats", "89 Pasture Way", "US", "Pasture-raised meats and house-made sausages."),
            ("Fresh Herb Gardens", "22 Lavender Dr", "US", "Culinary herbs grown in greenhouse tunnels."),
            ("Blueberry Ridge", "5 Forest Track", "US", "Specialized berry farm with premium harvests."),
            ("Riverbend Produce", "67 Valley Route", "US", "Wholesale-quality vegetables for local markets."),
            ("Golden Grain Mill", "140 Millstone Rd", "US", "Stone-ground flours and grain blends."),
            ("Harvest Moon Orchards", "9 Apple Court", "US", "Tree fruits including apples, pears, and plums."),
            ("Pure Spring Beverages", "200 Spring Blvd", "US", "Cold-pressed juices and natural beverages."),
            ("Seaside Shellfish", "17 Dockside Pier", "US", "Fresh shellfish and seafood prepared for retail."),
            ("Fieldstone Veg Co.", "73 Country Mile", "US", "Root vegetables and leafy greens year-round."),
            ("Hillside Poultry", "53 Coop Lane", "US", "Free-range poultry and eggs from local flocks."),
            ("Spice Trail Farms", "24 Saffron St", "US", "Dried spices and seasoning blends."),
            ("Morning Dew Greens", "96 Sunrise Road", "US", "Hydroponic greens and salad mixes."),
            ("Countryside Snacks", "11 Walnut Avenue", "US", "Nut mixes, dried fruits, and snack packs."),
            ("Lakeside Creamery", "8 Creamery Row", "US", "Yogurt, butter, and cultured dairy products."),
        ]

        product_templates = [
            ("Honeycrisp Apples", Product.ProductCategory.FRUITS, Product.UnitChoices.KG, "Crisp, sweet apples harvested this week."),
            ("Roma Tomatoes", Product.ProductCategory.VEGETABLES, Product.UnitChoices.KG, "Vine-ripened tomatoes suitable for salads and sauces."),
            ("Blueberries", Product.ProductCategory.BERRIES, Product.UnitChoices.G, "Fresh-picked berries in small batches."),
            ("Fresh Basil", Product.ProductCategory.HERBS, Product.UnitChoices.PCS, "Aromatic basil bunches for cooking."),
            ("Smoked Paprika", Product.ProductCategory.SPICES, Product.UnitChoices.G, "Mildly smoky ground paprika."),
            ("Whole Wheat Flour", Product.ProductCategory.FLOURS, Product.UnitChoices.KG, "Stone-milled whole wheat flour."),
            ("Grass-fed Beef", Product.ProductCategory.MEAT, Product.UnitChoices.KG, "Lean cuts from pasture-raised cattle."),
            ("Farmhouse Cheese", Product.ProductCategory.DAIRY, Product.UnitChoices.G, "Semi-hard cheese aged 60 days."),
            ("Atlantic Cod", Product.ProductCategory.FISH, Product.UnitChoices.KG, "Fresh cod fillets on ice."),
            ("Mussels", Product.ProductCategory.SEAFOOD, Product.UnitChoices.KG, "Live mussels cleaned and packed."),
            ("Sourdough Loaf", Product.ProductCategory.BAKERY, Product.UnitChoices.PCS, "Naturally leavened sourdough bread."),
            ("Apple Cider", Product.ProductCategory.BEVERAGES, Product.UnitChoices.L, "Unfiltered cider from local apples."),
            ("Trail Mix", Product.ProductCategory.SNACKS, Product.UnitChoices.G, "Roasted nuts and dried fruit blend."),
            ("Seasonal Special", Product.ProductCategory.OTHERS, Product.UnitChoices.PCS, "Limited seasonal market product."),
        ]

        market_locations = [
            "Central Square",
            "Riverside Pavilion",
            "Old Town Plaza",
            "Harbor Front",
            "Green Park",
            "Northside Community Hall",
            "Willow Street Market",
            "Lakeshore Promenade",
            "Maple Junction",
            "Sunset Court",
        ]
        market_types = [choice[0] for choice in MarketDay.MarketType.choices]

        for i in range(Producer.objects.count(), 20):
            name, address, country, desc = producer_blueprints[i % len(producer_blueprints)]
            suffix = f" {i + 1}" if i >= len(producer_blueprints) else ""
            final_name = f"{name}{suffix}"
            slug = final_name.lower().replace(" ", "-").replace(".", "")

            Producer.objects.create(
                name=final_name,
                address=address,
                country=country,
                description=desc,
                contact=f"Contact Person {i + 1}",
                email=f"producer{i + 1}@farmersmarket.local",
                phone=f"+1-555-01{i:02d}",
                website=f"https://{slug}.example.com",
            )

        producers = list(Producer.objects.order_by("id"))

        for i in range(Product.objects.count(), 20):
            pname, category, unit, desc = product_templates[i % len(product_templates)]
            producer = producers[i % len(producers)]

            Product.objects.create(
                name=f"{pname} Batch {i + 1}",
                description=desc,
                category=category,
                price=Decimal(f"{random.uniform(2.5, 35.0):.2f}"),
                quantity=random.randint(20, 350),
                unit=unit,
                producer=producer,
                expiry_date=date.today() + timedelta(days=random.randint(7, 120)),
            )

        for i in range(MarketDay.objects.count(), 20):
            event_date = date.today() + timedelta(days=i)
            open_dt = timezone.make_aware(datetime.combine(event_date, time(8 + (i % 3), 0)))
            close_dt = timezone.make_aware(datetime.combine(event_date, time(16 + (i % 3), 0)))

            market_day = MarketDay.objects.create(
                date=event_date,
                location=market_locations[i % len(market_locations)],
                market_type=market_types[i % len(market_types)],
                description=f"Weekly community market event #{i + 1} with local producers and seasonal goods.",
                market_open=open_dt,
                market_close=close_dt,
            )
            assigned_producers = random.sample(producers, k=random.randint(5, min(12, len(producers))))
            market_day.producers.add(*assigned_producers)

        self.stdout.write(self.style.SUCCESS(f"Producer records: {Producer.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Product records: {Product.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"MarketDay records: {MarketDay.objects.count()}"))
