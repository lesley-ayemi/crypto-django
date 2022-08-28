from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django_email_verification import send_email

from accounts.models import CustomUser

class UserRegisterView(TemplateView):
    template_name = 'auth/register.html'
        
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if not CustomUser.objects.filter(email=email).exists():
            if password == confirm_password:
                user = get_user_model().objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
                user.set_password(password)
                user.is_active = False
                # user.save()
                send_email(user)
                return render(request, 'confirm_template.html')
                # activateEmail(request, user, email)
                # return redirect('home')
            else:
                return HttpResponse('Password mismatch')
        else:
            return HttpResponse('Email is already taken')
        


class UserLoginView(TemplateView):
    template_name = "auth/login.html"
    
    def get(self, request):
        # logout(request)
        if request.user.is_authenticated:
            email = password = ''
            return redirect('home')
        else:
            return render(request, self.template_name)
            
        
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Error logging in')
        else:
            return HttpResponse('User does not exist')
    

