from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save
from .models import Contact
from django.conf import settings

@receiver(post_save, sender=Contact)
def partnership_notification (sender, instance, created, **kwargs):
    if created :
        subject = "New Message Alert"
        message = f"""Hi, Admin.

You have a new message from {instance.name}. Other details are
Name: {instance.name} 
Email: {instance.email}       
Kindly find their message below:
{instance.message}

Regards,
StreetKidsCan Support Team   
"""
        email_from = settings.DEFAULT_FORM_EMAIL
        email_to = ['omotundeakinsola@gmail.com']
        
        send_mail(subject=subject, message=message, from_email=email_from, recipient_list=email_to)