from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Project

# Create your views here.
@login_required(login_url='/login')
def index(request):
    current_user = request.user
    projects = Project.get_projects()
    return render(request, 'index.html', {'current_user':current_user, 'projects':projects})

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

