from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from FarmersMarket.markets.forms import MarketCreateForm, MarketUpdateForm, MarketDeleteForm
from FarmersMarket.common.forms import SearchForm
from FarmersMarket.markets.models import MarketDay

class MarketCreateView(CreateView):
    model = MarketDay
    form_class = MarketCreateForm
    template_name = 'markets/add-market.html'
    success_url = reverse_lazy('markets:list')


class MarketUpdateView(UpdateView):
    model = MarketDay
    form_class = MarketUpdateForm
    template_name = 'markets/update-market.html'
    success_url = reverse_lazy('markets:list')


class MarketDeleteView(DeleteView):
    model = MarketDay
    form_class = MarketDeleteForm
    template_name = 'markets/market_confirm_delete.html'
    success_url = reverse_lazy('markets:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs


class MarketListView(ListView):
    model = MarketDay
    template_name = 'markets/markets.html'

    def get_queryset(self):
        queryset = MarketDay.objects.prefetch_related('producers').all()
        self.search_form = SearchForm(self.request.GET)

        if self.search_form.is_valid():
            search_text = self.search_form.cleaned_data.get('search_text')
            if search_text:
                queryset = queryset.filter(location__icontains=search_text)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = getattr(self, 'search_form', SearchForm())
        return context


class MarketDetailView(DetailView):
    model = MarketDay
    template_name = 'markets/market-detail.html'


