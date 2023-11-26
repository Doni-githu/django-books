from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_welcome_email(email):
    subject = 'Welcome to My Website'
    message = 'Thank you for joining our website. We hope you have a great experience!'
    from_email = 'ddonierov96@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)