import datetime
import random

from django.core.management.base import BaseCommand
from mainapp.models import Employee, Unit
from faker import Faker

faker = Faker()


class Command(BaseCommand):
    help = 'Заполняет базу данных'

    def handle(self, *args, **kwargs):
        units = Unit.objects.all().count()
        employess = Employee.objects.all().count()
        if units == 0 and employess == 0:
            self.create_units()
            self.create_employees()

    def create_employees(self):
        rows_in_query = 5000

        def generate_record():
            units = Unit.objects.all()
            for i in range(rows_in_query):
                date = faker.date_between(start_date='-15y', end_date='now')
                yield Employee(fio='Employee' + str(i), salary=i*10, post='Post' + str(i),
                               employment_date=date, unit=units[i % 25])

        for i in range(10):
            Employee.objects.bulk_create(
                generate_record()
            )
            print('Создано сотрудников:{}'.format(i*5000))

    def create_units(self):
        units = []
        unit = Unit.objects.create(title='Unit')
        units.append(unit)
        for i in range(5):
            unit = Unit.objects.create(title='Unit'+str(i), parent=units[i])
            units.append(unit)
        for i in range(5, 25):
            Unit.objects.create(title='Unit' + str(i), parent=random.sample(units, 1)[0])

