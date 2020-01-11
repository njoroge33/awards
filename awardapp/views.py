from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    name = 'Signup'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name':name})

