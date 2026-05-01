from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import JobPost, Application, Feedback
from .forms import UserRegisterForm 

def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = JobPost.objects.filter(job_title__icontains=search_query) | \
               JobPost.objects.filter(company_name__icontains=search_query)
    else:
        jobs = JobPost.objects.all().order_by('-posted_on')

    applied_jobs = []
    if request.user.is_authenticated:
        applied_jobs = Application.objects.filter(student=request.user).values_list('job_id', flat=True)

    return render(request, 'home.html', {'jobs': jobs, 'applied_jobs': applied_jobs})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created! Welcome, {user.username}.")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    
    user_applications = Application.objects.filter(student=request.user).select_related('job')
    return render(request, 'dashboard.html', {'applications': user_applications})

@login_required
def apply_now(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    
    
    if not hasattr(request.user, 'profile'):
        messages.error(request, "Please complete your profile details first!")
        return redirect('home')

    
    application, created = Application.objects.get_or_create(
        student=request.user, 
        job=job
    )
    
    if created:
        messages.success(request, f"Application for {job.job_title} sent!")
    else:
        messages.warning(request, "You have already applied for this position.")
        
    return redirect('home')

@login_required
def rate_experience(request):
    if request.method == 'POST':
        rating_val = request.POST.get('rating')
        feedback_text = request.POST.get('feedback')
        if rating_val:
            Feedback.objects.create(user=request.user, rating=rating_val, comment=feedback_text)
            messages.success(request, "Thank you for your feedback!")
            return redirect('home')
    return render(request, 'rate_experience.html')