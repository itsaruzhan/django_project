from django.shortcuts import get_object_or_404, render,redirect 
from .models import *
from .forms import Clothesform, Customsform, NewUserForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login,  authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
    if request.method == 'POST':
       
        form = NewUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
           
            
            user.profile.country = form.cleaned_data.get('country')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.phoneNumber = form.cleaned_data.get('phoneNumber')
            user.profile.save
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'polls/registration.html', {'register_form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="polls/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def customs(request):
    customs = Customs.objects.all
    return  render(request, "polls/customs.html" , {'title': 'Traditional Customs', 'customs': customs})
def home(request):
    home = Home.objects.all
    return  render(request, "polls/home.html", {'title': 'Home page', 'home': home, })
def about(request):
    about= Questions.objects.all
    return  render(request, "polls/about.html", {'title': 'About', 'about': about, })
def registration(request):
    return  render(request, "polls/registration.html", {'title': 'Registration'})



def create_clothes(request):
    form = Clothesform()
    if request.method == "POST":
        form = Clothesform(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('/show_clothes')
            except:
                message = "Something we are wrong!"
                form = Clothesform()
            return render(request, 'polls/create.html',{'message':message,'form':form})
    else:
        form = Clothesform()
    return render(request, 'polls/create.html',{'form':form})

def show_clothes(request):
    cloth = Clothes.objects.order_by('id')
    return render(request, 'polls/index.html', {'cloth':cloth})

def edit_clothes(requst, id):
    cloth = Clothes.objects.get(id=id)
    return render(requst, 'polls/edit.html',{'cloth':cloth})

def update_clothes(request, id):
    cloth = Clothes.objects.get(id=id)
    if request.method == "POST" :
        form = Clothesform(request.POST, request.FILES, instance = cloth)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("/show_clothes")
        message = 'Something we are wrong!'
        return render(request, 'polls/edit.html',{'message':message,'cloth':form})
    else:
        form = Clothes.objects.get(id=id)
        cloth = Clothesform(instance = form)
        content = {'cloth':cloth,'id':id}
        return render(request, 'polls/edit.html',content)

def delete_clothes(request, id):
    cloth = Clothes.objects.get(id=id)
    cloth.delete()
    messages.success(request, 'Deleted successful!')
    return redirect("/show_clothes")



def create_customs(request):
    form = Customsform()
    if request.method == "POST":
        form = Customsform(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('/show_customs')
            except:
                message = "Something we are wrong!"
                form = Customsform()
            return render(request, 'polls/create2.html',{'message':message,'form':form})
    else:
        form = Clothesform()
    return render(request, 'polls/create2.html',{'form':form})

def show_customs(request):
    custom = Customs.objects.order_by('id')
    return render(request, 'polls/index2.html', {'custom':custom})

def edit_customs(requst, id):
    custom = Customs.objects.get(id=id)
    return render(requst, 'polls/edit2.html',{'custom':custom})

def update_customs(request, id):
    custom = Customs.objects.get(id=id)
    if request.method == "POST" :
        form = Customsform(request.POST, request.FILES, instance = custom)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("/show_customs")
        message = 'Something we are wrong!'
        return render(request, 'polls/edit2.html',{'message':message,'custom':form})
    else:
        form = Customs.objects.get(id=id)
        custom = Customsform(instance = form)
        content = {'custom':custom,'id':id}
        return render(request, 'polls/edit2.html',content)

def delete_customs(request, id):
    custom = Customs.objects.get(id=id)
    custom.delete()
    messages.success(request, 'Deleted successful!')
    return redirect("/show_customs")    
# Create your views here.
