from django.shortcuts import render, redirect
from app.forms import UserForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
   return render(request, 'app/base.html')

def ilsan(request):
    return render(request, 'app/ilsan.html') 

def busan(request):
    return render(request, 'app/busan.html') 

def faq(request):
    return render(request, 'app/FAQ.html')

def schedule(request):
    return render(request, 'app/schedule.html')  

def setec_site(request):
    return render(request, 'app/setec_site.html') 

def setec(request):
    return render(request, 'app/setec.html') 

def suwon(request):
    return render(request, 'app/suwon.html') 

def bexcosite(request):
    return render(request, 'app/bexcosite.html') 

def kintexsite(request):
    return render(request, 'app/kintexsite.html') 

def note(request):
    return render(request, 'app/note.html') 

def price(request):
    return render(request, 'app/price.html') 

def suwonsite(request):
    return render(request, 'app/suwonsite.html') 

def team(request):
    return render(request, 'app/team.html') 






def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      raw_password = form.cleaned_data.get('password1')
 
      user = authenticate(username=username, first_name=first_name, last_name=last_name, password=raw_password)
      login(request, user)
      return redirect('/')
  else:
    form = UserForm()
  return render(request, 'app/signup.html', {'form':form})