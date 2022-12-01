from django.contrib import admin
from django.urls import path
from mainapp.views import EmployeeByUnitView, UnitListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UnitListView.as_view(), name='unit-list'),
    path('unit/<str:id>/', EmployeeByUnitView.as_view(), name='employee-by-unit'),
    ]
