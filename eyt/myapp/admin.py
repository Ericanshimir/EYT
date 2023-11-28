from django.contrib import admin
from .models import Feature
from .models import Chart

# Register your models here.
admin.site.register(Feature)
admin.site.register(Chart)