from django.contrib import admin
from bathroomapp.models import AppUser, Packages, Bathroom

# Register your models here.

admin.site.register(AppUser)
admin.site.register(Packages)
admin.site.register(Bathroom)
