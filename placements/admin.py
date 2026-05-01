from django.contrib import admin
from .models import StudentProfile, JobPost, Application, Feedback

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'cgpa')
    search_fields = ('user__username', 'branch')
    list_filter = ('branch',)

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'salary_lpa', 'posted_on')
    search_fields = ('job_title', 'company_name')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    
    list_display = ('student', 'job', 'status', 'applied_on')
  
    list_editable = ('status',) 
    list_filter = ('status', 'job__company_name')
    search_fields = ('student__username', 'job__job_title')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')
    readonly_fields = ('created_at',)

