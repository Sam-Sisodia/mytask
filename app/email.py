from cgitb import text



from django.core.mail import send_mail
from . models import *

from django.conf  import settings
from templates import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Verification email 

def Verification_email(email,token):
    #html_tmp_path = "templates/email.html"
    try:
        html_content = render_to_string("emailverify.html",{'token':token})
        text_content = strip_tags(html_content)

        email =EmailMultiAlternatives(
            "Verification mail",text_content,settings.EMAIL_HOST,[email]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        print("Message Sent")
    except Exception as e:
        return False
    return True