from django.shortcuts import render
# from django.template.context_processors import request

from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request):
        common_result = None
        result = None
        if request.method == 'GET':
            form = CalcForm(request.GET)

            if form.is_valid():
                initial_fee = int(request.GET['initial_fee'])
                rate = int(request.GET['rate'])
                months_count = int(request.GET['months_count'])
                common_result = round((initial_fee + initial_fee * rate) / months_count)
                result = round(common_result / months_count)

            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'common_result': common_result,
                    'result': result,
                },
            )
