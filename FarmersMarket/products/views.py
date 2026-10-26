from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from FarmersMarket.products.forms import ProductCreateForm, ProductUpdateForm, ProductDeleteForm
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
    form_class = ProductDeleteForm
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs


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
