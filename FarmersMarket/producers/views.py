from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from FarmersMarket.producers.forms import ProducerCreateForm, ProducerUpdateForm
from FarmersMarket.producers.models import Producer
from FarmersMarket.common.forms import SearchForm

class ProducerCreateView(CreateView):
    model = Producer
    form_class = ProducerCreateForm
    template_name = 'producers/add-producer.html'
    success_url = reverse_lazy('producers:list')

class ProducerUpdateView(UpdateView):
    model = Producer
    form_class = ProducerUpdateForm
    template_name = 'producers/update-producer.html'
    success_url = reverse_lazy('producers:list')


class ProducerDeleteView(DeleteView):
    model = Producer
    success_url = reverse_lazy('producers:list')


class ProducerListView(ListView):
    model = Producer
    template_name = 'producers/producers.html'

    def get_queryset(self):
        queryset = Producer.objects.prefetch_related('products').all()
        self.search_form = SearchForm(self.request.GET)

        if self.search_form.is_valid():
            search_text = self.search_form.cleaned_data.get('search_text')
            if search_text:
                queryset = queryset.filter(name__icontains=search_text)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = getattr(self, 'search_form', SearchForm())
        return context


class ProducerDetailView(DetailView):
    model = Producer
    template_name = 'producers/producer-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = (
            self.object.products
            .all()
            .order_by('name')
        )
        return context

