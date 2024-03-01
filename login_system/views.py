from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import View
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import generate_token
from django.utils.encoding import force_bytes,force_str
from django.conf import settings

# Create your views here.

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']

        if password != confirm_password:
            messages.warning(request,"Password Not Matching")
            return redirect("/auth/signup")
        
        
        if User.objects.filter(email=email).first():
            messages.warning(request,"Email already exists")
            return redirect("/auth/signup")
    
        user = User.objects.create_user(username, email=email, password=password)
        user.is_active =False
        user.save()

        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)

        })

        send_mail_to_user(message=message, email=email)
        messages.success(request,"Verify your Email.")
        return redirect('/auth/signup')
        
    return render(request, "signup.html")

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password= request.POST['pass1']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("/")
        
        else:
            messages.warning(request,"Invalid crediantials.")
            return redirect("/auth/login")
    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect("/")

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/auth/login')
        messages.success(request,"Something wet wrong.")
        return render(request,'login.html')



    
def send_mail_to_user(email,message):
    subject = 'Your account need to be verified.'
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )