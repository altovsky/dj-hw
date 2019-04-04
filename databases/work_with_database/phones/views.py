from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template_name = 'catalog.html'
    context = {}

    sort_type = request.GET.get('sort')
    ph = Phone.objects.all()

    if sort_type == 'name':
        ph = ph.extra(order_by=['name'])
    elif sort_type == 'min_price':
        ph = ph.extra(order_by=['price'])
    elif sort_type == 'max_price':
        ph = ph.extra(order_by=['-price'])

    context['phones'] = ph
    context['site_url'] = f"{request.scheme}://{request.META['HTTP_HOST']}/catalog"

    return render(
        request,
        template_name,
        context,
    )


def show_product(request, slug):
    template_name = 'product.html'
    context = {}

    ph = Phone.objects.get(slug=slug)
    context['phone'] = ph

    return render(
        request,
        template_name,
        context,
    )
