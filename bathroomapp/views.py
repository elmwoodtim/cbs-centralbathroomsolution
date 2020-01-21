from django.shortcuts import render

# Create your views here.

def home(request):
    data = dict()
    data['help'] = "Help Text"
    data['yelp'] = "Yelp Text"

    import datetime
    data['date'] = datetime.date.today()

    return render(request, "home.html", context=data)