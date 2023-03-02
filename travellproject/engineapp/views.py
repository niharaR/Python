from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages,auth
from django.shortcuts import render
# from django.contrib.auth import login, authenticate

def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
          auth.login(request,user)
          return redirect('/')
       else:
         messages.info(request,"invalid")
         return redirect('login')
    else:
       return render(request,"login.html")

# #
#
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if   User.objects.filter(username=username).exists():
                 messages.info(request, "username taken")

            else:
                  user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                  user.save();
                  print("user created")
            return redirect('register')


        else:
                  messages.info(request,"password not matching")
                  return redirect('register')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

