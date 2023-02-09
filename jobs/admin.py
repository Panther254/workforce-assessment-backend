from django.contrib import admin
from .models import Job, JobApplication, Position, TechStack

admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Position)
admin.site.register(TechStack)


