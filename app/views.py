from django.shortcuts import render ,HttpResponse,redirect

from django.contrib import messages

# Create your views here.
import uuid
from . email  import *

from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout
from django.core.mail import send_mail,EmailMessage

from .models import *
def RegisterUser(request,):
    form  = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = request.POST.get('email')
            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()
            user.email_token = str(uuid.uuid4())
            user.save()

            Verification_email(email,user.email_token)
            return redirect('login')

    
           
        else:
            form  = UserRegisterForm(request.POST)
            print(form.errors)
            return render(request,'register.html',locals())
        
    return render(request,'register.html')




# def  edituserdetails(request,id ,data=None):
#     obj = Myuser.objects.get(id=id)
#     if data == "delete":
#         obj.delete()
    
#     return render(request,'register.html')
    




def Login(request):
    if  request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
        user = authenticate(request,email=email,password=password)

        if user is not None:
            auth_login(request, user)
            user=request.user
            if user.is_varified == True:
                return render(request,'dashboard.html')

            else:
                messages.info(request ,"Please Verify Your Accounts ")
        else:
            #return HttpResponse("User Not ragister ")
            messages.info(request ,"Incorrect Username or Password")
            return render(request, 'login.html')
    return render(request,'login.html')


def Dashboard(request):
    return render(request,'dashboard.html')




def verifyaccount(request,token):
    try:
        obj = User.objects.get(email_token=token )
        obj.is_varified=  True
        obj.save()
        return HttpResponse("Verifie  Suessfully")

    except Exception as e:
        return HttpResponse("<h1> Invalid Token </h1>")


def sendinvoice(request):
    if request.method == "POST":
        # subject = request.POST.get("subject")
        # print(subject)
        rceiveremail= request.POST.get("rceiveremail")
        print(rceiveremail)
        discription = request.POST.get("discription")
        print(discription)
        userfile = request.FILES['userfile']
        





        
        email =EmailMessage(
            "Verification mail","Hello",settings.EMAIL_HOST,[rceiveremail],)
        email.content_subtype="html"
        file = request.FILES['userfile']
        email.attach(file.name, file.read(),file.content_type)
   
        email.send()

        return HttpResponse("Done hai bro ")

    
    return  render(request, 'sendinvoice.html')



def createinvoice(request):
    return  render(request, 'createinvoice.html')
    
