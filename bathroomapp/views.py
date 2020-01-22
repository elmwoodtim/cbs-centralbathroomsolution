from django.shortcuts import render

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

def new_user_register(request):
    return render(request, "register.html")

def guest(request):
    return render(request, "guest.html")

def guest_stuff(request):
    data = dict()
    return render(request, "guest_stuff.html", context=data)

