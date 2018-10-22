from django.contrib import admin

from .models import CollegeDetails,Facilites,Admissions,Approvals,Aluminis

admin.site.register(CollegeDetails)
admin.site.register(Facilites)
admin.site.register(Admissions)
admin.site.register(Approvals)
admin.site.register(Aluminis)