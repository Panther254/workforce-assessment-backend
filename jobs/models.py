from django.db import models


class Job(models.Model):
    REMOTE = 'REMOTE'
    ONSITE = 'ONSITE'

    JOB_TYPE_CHOICES = [
        (REMOTE, 'Remote'),
        (ONSITE, 'Onsite'),
    ]

    company_logo = models.ImageField(upload_to='company_logos')
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
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes')
    cover_letter = models.TextField()

    def __str__(self):
	    return "Applied by " + self.name 


