from django.views.generic import TemplateView
from FarmersMarket.markets.models import MarketDay
from FarmersMarket.producers.models import Producer
from FarmersMarket.products.models import Product

class HomePageView(TemplateView):
    template_name = "common/home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "total_products": Product.objects.count(),
            "total_producers": Producer.objects.count(),
            "total_market_days": MarketDay.objects.count(),
            "latest_products": Product.objects.select_related("producer").order_by("-created_at")[:5],
            "upcoming_market_days": MarketDay.objects.order_by("date")[:5],
        })
        return context

