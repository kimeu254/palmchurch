from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('welcome')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm
        context['registration_form'] = form
        return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect()

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("welcome")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('welcome')

    else:
        form = AccountAuthenticationForm

    context['login_form'] = form
    return render(request, 'account/login.html', context)