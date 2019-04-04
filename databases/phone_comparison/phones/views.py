from django.shortcuts import render
from .models import Phone, Xiaomi, Motorola, Alcatel


def show_catalog(request):
    template_name = 'catalog.html'
    context = {}
    # context = super().get_context_data(**kwargs)

    phones = Phone.objects.all()
    xiaomi = Xiaomi.objects.all()
    context['phones'] = phones
    context['xiaomi'] = xiaomi

    return render(
        request,
        template_name,
        context,
    )
