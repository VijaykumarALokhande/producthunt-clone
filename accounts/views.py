from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method=='POST':
        existing_user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if existing_user is not None:
            auth.login(request, existing_user)
            return redirect('firsthomepage')
        else:
            return render(request, 'accounts/login.html', {'error':'invalid creadential or user DoesNotExist'})
    else:
        return render(request, 'accounts/login.html')





def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                existing_user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken.'})
            except User.DoesNotExist:
                new_user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, new_user)
                return redirect('firsthomepage')
            return render(request, 'accounts/signup.html', {'error':'Post password matched'})
        else:
            return render(request, 'accounts/signup.html', {'error':'PoST  unmatced passwords'})
    else:
        return render(request, 'accounts/signup.html')




def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('firsthomepage')
