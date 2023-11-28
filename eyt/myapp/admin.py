from django.contrib import admin
from .models import Feature
from .models import Chart
from .models import Video

# Register your models here.
admin.site.register(Feature)
admin.site.register(Chart)
admin.site.register(Video)
