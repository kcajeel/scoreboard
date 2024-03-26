from django.contrib import admin

from .models import teams
from .models import service_checks
from .models import check_details

# Register your models here.
admin.site.register(teams)
admin.site.register(service_checks)
admin.site.register(check_details)