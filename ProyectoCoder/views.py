from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from .forms import UserRegisterForm


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.data.get('username')
            passwd = form.data.get('password')

            user = authenticate(username=usuario, password=passwd)

            if user:
                login(request, user)

                return redirect('List')
            else:
                return redirect('New')

        else:
            return redirect('New')
    
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        

        if form.is_valid():
            
            username = form.data['username']
            form.save()

            return redirect('Login')

    else:
        print('asdfasdfadsf')        
        # form = UserCreationForm()
        form = UserRegisterForm(request.POST)

    return render(request, 'register.html', {'form': form})
