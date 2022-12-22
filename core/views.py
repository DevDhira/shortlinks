from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Links
import randomcharactergenerator


# Create your views here.
def home(request):
    return render(request,'core/home.html')

def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('app')
    
    return render(request,'core/signup.html',context={'form':form})

@login_required
def app(request):
    links = Links.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        unique_code = randomcharactergenerator.rand_code(7)
        if not Links.objects.filter(unique_code=unique_code).exists():
            shroten_url = str(request.scheme) + '://' + str(request.META["HTTP_HOST"])+"/r/"+str(unique_code)
            Links.objects.create(name=name, link=url, unique_code=unique_code, shorten_link = shroten_url, created_by=request.user)
            messages.success(request, "Link Created Succcessfully")
            return redirect('app')
    
    return render(request, 'core/app.html',{'links':links})
    

def redirect_link(request,unique_code):
    link = Links.objects.get(unique_code=unique_code)

    link.visits+=1
    link.save()
    return redirect(link.link)

def delete_link(request,unique_code):
    Links.objects.filter(unique_code=unique_code).delete()

    return redirect('app')