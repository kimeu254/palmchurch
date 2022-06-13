from django.shortcuts import render

# Create your views here.

def welcome_screen_view(request):
    print(request.headers)
    return render(request, 'base.html', {})