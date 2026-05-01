from django.contrib import admin
from django.urls import path, include
from placements import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('admin/', admin.site.urls),

  
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/<int:job_id>/', views.apply_now, name='apply_now'),
    path('rate-experience/', views.rate_experience, name='rate_experience'),

   
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    
    
  
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='emails/password_reset.html'), 
         name='password_reset'),
    
   
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='emails/password_reset_done.html'), 
         name='password_reset_done'),
    
    
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='emails/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    
    
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='emails/password_reset_complete.html'), 
         name='password_reset_complete'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 