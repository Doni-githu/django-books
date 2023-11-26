from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from celery import shared_task
from config.celery import app

@app.task
def send_welcome_email(email):
    subject = 'Welcome to My Website'
    message = 'Thank you for joining our website. We hope you have a great experience!; Cool'
    from_email = EMAIL_HOST_USER
    recipient_list = [email]
    result = send_mail(subject, message, from_email, recipient_list)
    return True