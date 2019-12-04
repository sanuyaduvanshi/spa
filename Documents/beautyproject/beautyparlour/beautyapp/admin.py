from django.contrib import admin

# Register your models here.
from  .models import Citys
from .models import Services
admin.site.register(Citys)
admin.site.register(Services)
