from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template



def send_email(recipient_list=None):
    subject = 'Test email!'
    message = 'Thank you for working for us!'
    email_from = settings.EMAIL_HOST_USER

    template = get_template('email.html')

    send_mail(subject, email_from, message, recipient_list, html_message=template.render())
