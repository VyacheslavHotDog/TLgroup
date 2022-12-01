from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Employee, Unit


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, PostAdmin)


class CategoryAdmin(MPTTModelAdmin):
    pass


admin.site.register(Unit, CategoryAdmin)
