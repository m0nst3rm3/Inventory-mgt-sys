from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from .models import SignUpForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # forms.save()
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('lastname')
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            retype_password = form.cleaned_data['retype_password']
            if password == retype_password:
                user = authenticate(firstname=firstname, lastname=lastname,
                                    password=password, username=username,
                                    email=email, address=address,
                                    )
                login(request, user)
                # SignUpForm.objects.create(user=user)
            return redirect('login')
    context = {
        'forms': form
    }
    return render(request, 'users/signup.html', context)
