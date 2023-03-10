from django.db import models


default_logo = "https://res.cloudinary.com/dvzbsqkfs/image/upload/v1675945846/workforce_assessment/media/company_logos/logo_speksk.png"

class Job(models.Model):
    REMOTE = 'REMOTE'
    ONSITE = 'ONSITE'

    JOB_TYPE_CHOICES = [
        (REMOTE, 'Remote'),
        (ONSITE, 'Onsite'),
    ]

    company_logo_url = models.URLField(max_length=300,default=default_logo)
    company_title = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    sector = models.CharField(max_length=50)
    number_of_employees = models.IntegerField()
    date_posted = models.DateField(auto_now_add=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
	    return self.job_title

class Position(models.Model):
   
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job,on_delete=models.CASCADE, related_name='positions')

    def __str__(self):
	    return self.name

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    job = models.ForeignKey(Job,on_delete=models.CASCADE, related_name='techstacks')
    
    def __str__(self):
	    return self.name


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    date_applied = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume_link = models.URLField(max_length=200, default="")
    cover_letter = models.TextField()

    def __str__(self):
	    return "Applied by " + self.name 


