from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Family)
admin.site.register(models.Location)
admin.site.register(models.Transaction)