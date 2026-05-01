from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    branch = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skills = models.TextField(help_text="Enter skills separated by commas")

    def __str__(self):
        return f"{self.user.username}'s Profile"

class JobPost(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    description = models.TextField()
    salary_lpa = models.FloatField(verbose_name="Package in LPA")
    min_cgpa_required = models.DecimalField(max_digits=4, decimal_places=2)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    class Meta:
        
        unique_together = ('student', 'job')

    def __str__(self):
        return f"{self.student.username} -> {self.job.job_title}"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.rating} by {self.user.username}"