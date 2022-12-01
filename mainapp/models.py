from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Employee(models.Model):
    fio = models.CharField(max_length=150, verbose_name='Фио', unique=True)
    post = models.CharField(max_length=150, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Зарплата')
    employment_date = models.DateField(verbose_name='Дата приема')
    unit = TreeForeignKey('Unit', on_delete=models.PROTECT, related_name='employees', verbose_name='Категория')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Unit(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительское подразделение')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def get_absolute_url(self):
        return reverse('employee-by-unit', args=[str(self.id)])

    def __str__(self):
        return self.title