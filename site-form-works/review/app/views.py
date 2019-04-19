from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                # if not request.session['reviewed_products']:
                print(request.session['reviewed_products'])
                request.session['reviewed_products'] = []
                request.session['reviewed_products'].append(Product.pk)
                print(form.is_valid())

                pass
                return redirect('/')
        else:
            form = ReviewForm()

        return form

    # def get_queryset(self):
    #
    #     r = self.model.objects.prefetch_related()
    #     return r
