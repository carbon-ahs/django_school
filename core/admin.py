from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.School)
admin.site.register(models.Teacher)
admin.site.register(models.Notice)
admin.site.register(models.ClassRoutine)
admin.site.register(models.Stuff)
