from django.views.generic import ListView
from .models import Employee, Unit


class UnitListView(ListView):
    model = Unit
    template_name = "mainapp/unit_list.html"


class EmployeeByUnitView(ListView):
    context_object_name = 'employees'
    template_name = 'mainapp/employee_list.html'
    paginate_by = 30

    def get_queryset(self):
        self.unit = Unit.objects.get(pk=self.kwargs['id'])
        queryset = Employee.objects.filter(unit=self.unit)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.unit
        return context