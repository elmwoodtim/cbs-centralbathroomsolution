from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from bathroomapp.models import AppUser

# Create your views here.

def home(request):
    data = dict()
    data['help'] = "Help Text"
    data['yelp'] = "Yelp Text"

    persons = [
        ["John", "New York"], ["Abby", "Boston"], ["Peter", "Washington D.C."]
    ]

    data['people'] = persons

    import datetime
    data['date'] = datetime.date.today()

    return render(request, "home.html", context=data)

def login(request):
    return render(request, "registration/login.html")

def loggedin(request):
    data=dict()
    return render(request, "loggedIn.html", context=data)

def guest(request):
    return render(request, "guest.html")

def guest_data(request):
    try:
        request.GET['Cancel']
        return render(request, 'home.html')
    except:
        pass

    data = dict()
    name = request.GET['user.name']
    city = request.GET['user.city']
    dob = request.GET['user.dob']
    email = request.GET['user.email']
    data['name'] = name
    data['city'] = city
    data['dob'] = dob
    data['email'] = email
    return render(request, "guest_data.html", context=data)

def register_user(request):
    data = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email
        new_user.save()
        acct_holder = AppUser(user=new_user)
        acct_holder.points = 1000
        acct_holder.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        form = UserCreationForm()
        data['form'] = form
        return render(request, "registration/register.html", context=data)
