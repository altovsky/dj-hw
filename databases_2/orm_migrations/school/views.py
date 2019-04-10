from django.views.generic import ListView

from .models import Student


# class StudentListView(ListView):
#     model = Student
#     ordering = 'group'

class StudentListView(ListView):
    template_name = 'school/student_list.html'

    def get_queryset(self):

        v = Student.objects.prefetch_related()

        return v
