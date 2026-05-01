from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import Application

def send_corporate_email(subject, to_email, title, body_text, button_text=None, action_url=None):
    context = {
        'title': title,
        'body_text': body_text,
        'button_text': button_text,
        'action_url': action_url,
    }
    html_content = render_to_string('emails/corporate_email.html', context)
    text_content = strip_tags(html_content) # Fallback for old email clients

    email = EmailMultiAlternatives(subject, text_content, 'Udyoga Maya <noreply@udyogamaya.com>', [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

@receiver(post_save, sender=User)
def registration_email(sender, instance, created, **kwargs):
    if created:
        send_corporate_email(
            subject="Welcome to the Network",
            to_email=instance.email,
            title="Account Verified",
            body_text=f"Welcome {instance.username}! Your corporate profile for Udyoga Maya is now active. Explore premium job opportunities today.",
            button_text="Browse Jobs",
            action_url="http://127.0.0.1:8000/"
        )


@receiver(post_save, sender=Application)
def application_email(sender, instance, created, **kwargs):
    if created:
        send_corporate_email(
            subject="Application Confirmation",
            to_email=instance.student.email,
            title="Application Received",
            body_text=f"Your application for {instance.job.job_title} at {instance.job.company_name} has been successfully logged into our system.",
            button_text="View Dashboard",
            action_url="http://127.0.0.1:8000/dashboard/"
        )
    elif instance.status == 'Success':
        send_corporate_email(
            subject="Selection Update",
            to_email=instance.student.email,
            title="Congratulations!",
            body_text=f"We are pleased to inform you that your application for {instance.job.job_title} has been moved to SUCCESS status.",
            button_text="Check Details",
            action_url="http://127.0.0.1:8000/dashboard/"
        )