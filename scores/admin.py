from django.contrib import admin

from .models import teams, targets, ports

# Register your models here.
admin.site.register(teams)
admin.site.register(targets)
admin.site.register(ports)