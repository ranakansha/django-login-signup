from django.shortcuts import render,redirect
from dashboard.models import User
# from dashboard.forms import UserForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = User()
        count = User.objects.filter(email=email,password=password).count()
        if count >0:
            return redirect('/home')
        else:
            messages.error(request,'Invalid Email And Password')
            return redirect('/')

    return render(request,'login.html')

def user_register(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        obj = User(name=name,email=email,password=password,phone=phone)
        obj.save()

        messages.success(request,'you are register sucessfully')
        # return redirect('/')
    return render(request,'signup.html')


def home(request):
    return HttpResponse('testing.......')