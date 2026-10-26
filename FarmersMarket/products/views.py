from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from FarmersMarket.products.forms import ProductCreateForm, ProductUpdateForm
from FarmersMarket.common.forms import SearchForm
from FarmersMarket.products.models import Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/add-product.html'
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'products/update-product.html'
    success_url = reverse_lazy('products:list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_queryset(self):
        queryset = Product.objects.select_related('producer').all()
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
