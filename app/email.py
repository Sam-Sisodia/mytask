from cgitb import text



from django.core.mail import send_mail,EmailMessage
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



def Sendinvoicemail_email(rceiveremail):
    #html_tmp_path = "templates/email.html

    print("==================",rceiveremail)

    subject = 'Your account login Password mail'
    message = 'Your password '
    email_from = settings.EMAIL_HOST
#     send_mail(subject, message, email_from,[rceiveremail] )

# from pdf_mail import sendpdf

# def Sendinvoicemailpdf_email(rceiveremail,userfile):
#     #html_tmp_path = "templates/email.html
#     try:
#         print("==================",rceiveremail)

#         subject = 'Your account login Password mail'
#         message = 'Your password '
#         email_from = settings.EMAIL_HOST
#         email_message = EmailMessage(subject, message,email_from,[rceiveremail],)
#         email_message.attach_file([userfile])
#         email_message.send()
#     except Exception as e:
#         return False
#     return True







def Sendinvoicemailpdf_email(email,file):
    #html_tmp_path = "templates/email.html"
    try:
        #html_content = render_to_string("emailverify.html",)
    

        email =EmailMessage(
            "Verification mail","Hello",settings.EMAIL_HOST,[email],
        
        )
        email.content_subtype="html"
        
        email.attach(file.name, file.read(),file.content_type)

        email.send()

        print("Message Sent")
    except Exception as e:
        print("not send")
        return False
    return True
    
