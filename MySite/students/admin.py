from django.contrib import admin

# Register your models here.

from .models import Students


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "grade", "course", "enroll_date")


admin.site.register(Students, StudentAdmin)