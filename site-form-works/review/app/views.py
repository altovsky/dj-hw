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
        prod_key = kwargs['object'].id

        context = super().get_context_data(**kwargs)

        if 'reviewed_products' not in self.request.session:
            self.request.session['reviewed_products'] = []

        if prod_key in self.request.session['reviewed_products']:
            return context

        context['form'] = ReviewForm
        context['reviews'] = Review.objects.filter(product_id=prod_key)

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                prod_key = int(kwargs['pk'])

                rev = Review(text=form.cleaned_data['text'])
                prod = Product.objects.get(pk=prod_key)
                rev.product = prod
                rev.save()
                
                if prod_key not in request.session['reviewed_products']:
                    request.session['reviewed_products'].append(prod_key)
                    request.session.modified = True

                return redirect('/')
        else:
            form = ReviewForm()

        return form
