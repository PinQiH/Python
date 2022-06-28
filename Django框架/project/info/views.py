from django.shortcuts import render
from .scrapers import Facebook

def index(request):
 
    facebook = Facebook(request.POST.get("profile_url"))
 
    context = {
        "info": facebook.scrape()
    }
 
    return render(request, "info/index.html", context)