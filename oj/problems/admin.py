from django.contrib import admin
from .models import problem
# Register your models here.
class problemAdmin(admin.ModelAdmin):
    list_display=("problem_name","problem_statement")
admin.site.register(problem,problemAdmin)
