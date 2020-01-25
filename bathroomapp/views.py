from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from bathroomapp.models import AppUser, Packages, Bathroom


# Create your views here.

def home(request):
    data = dict()
    return render(request, "home.html", context=data)


def login(request):
    return render(request, "registration/login.html")


def loggedin(request):
    data = dict()
    user = request.user
    if user.is_superuser:
        return render(request, "admin_ops.html", context=data)

    packages = Packages.objects.all()
    packages_list = list()
    for p in packages:
        packages_list.append([p.packageId,p.description,p.location,p.min_bid])
    data['packages'] = packages_list

    bathrooms = Bathroom.objects.all()
    bathrooms_list = list()
    for b in bathrooms:
        bathrooms_list.append([b.bathroomId, b.location, b.description, b.gender, b.ratingOverall])
    data['bathrooms'] = bathrooms_list

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


def resort_finder(request):
    from bathroomapp.support_functions import get_resorts
    data = dict()
    resorts = get_resorts()
    data['data'] = resorts
    return render(request, "resorts.html", context=data)


def do_admin_stuff(request):
    data = dict()

    try:
        request.GET['bathrooms']
        file = request.GET['file']
        file = "static/bathroomapp/" + file
        with open(file, 'r') as f:
            for line in f:
                line = line.strip().split(',')
                b = Bathroom()
                b.description = line[1]
                b.location = line[2]
                b.latitude = float(line[3])
                b.longitude = float(line[4])
                b.gender = line[5]
                b.numStall = int(line[6])
                b.numUrinal = int(line[7])
                b.ratingOverall = int(line[8])
                b.ratingClean = int(line[9])
                b.ratingConv = int(line[10])
                b.save()
        data['message'] = "Completed bulk update of bathrooms!"
        return render(request, "admin_ops.html", context=data)
    except:
        pass
    try:
        request.GET['users']
        file = request.GET['file']
        file = "static/bathroomapp/" + file
        data['message'] = "Completed bulk update of users!"
        return render(request, "admin_ops.html", context=data)
    except:
        pass
    return render(request, "admin_ops.html", context=data)


def bathroom_map(request):
    data = dict()

    bathrooms = Bathroom.objects.all()
    bathrooms_list = list()
    for b in bathrooms:
        bathrooms_list.append([b.bathroomId, b.location, b.latitude, b.longitude, b.description, b.gender, b.ratingOverall])
    data['bathrooms'] = bathrooms_list

    return render(request, 'bathroom_map.html', context=data)


def add_bathroom(request):
    data = dict()
    return render(request, 'add_bathroom.html', context=data)

def added_bathroom(request):
    try:
        request.GET['Cancel']
        return render(request, 'home.html')
    except:
        pass

    data = dict()
    desc = request.GET['b.description']
    loc = request.GET['b.location']
    lat = request.GET['b.latitude']
    lng = request.GET['b.longitude']
    gender = request.GET['b.gender']
    ratingovr = request.GET['rate']
    numstall = request.GET['b.numStall']
    numurinal = request.GET['b.numUrinal']
    reqcode = request.GET['b.reqCode']
    securitycode = request.GET['b.securityCode']
    data['desc'] = desc
    data['loc'] = loc
    data['lat'] = lat
    data['lng'] = lng
    data['gender'] = gender
    data['ratingovr'] = ratingovr
    data['numStall'] = numstall
    data['numUrinal'] = numurinal
    data['reqCode'] = reqcode
    data['securityCode'] = securitycode

    b = Bathroom()
    b.description = desc
    b.location = loc
    b.latitude = lat
    b.longitude = lng
    b.gender = gender
    b.numStall = numstall
    b.numUrinal = numurinal
    b.ratingOverall = ratingovr
    b.save()

    for b in Bathroom.objects.all():
        print(b)
    return render(request, "added_bathroom.html", context=data)


def add_review(request):
    data = dict()

    bathrooms = Bathroom.objects.all()
    bathrooms_list = list()
    for b in bathrooms:
        bathrooms_list.append(
            [b.location, b.description, b.ratingOverall, b.bathroomId])
    data['bathrooms'] = bathrooms_list

    return render(request, "add_review.html", context=data)


def added_review(request):
    try:
        request.GET['Cancel']
        return render(request, 'home.html')
    except:
        pass
    data = dict()
    ratingovr = request.GET['rate']

    id = request.GET["b.id"]
    b = Bathroom.objects.get(bathroomId=id)
    b.ratingOverall = ratingovr
    b.save()

    desc = b.description
    ratingovr = b.ratingOverall
    data['desc'] = desc
    data['ratingovr'] = ratingovr
    data['id'] = id

    return render(request, "added_review.html",context=data)

