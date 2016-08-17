from django.shortcuts import render
from .forms import SearcherForm
from .models import Searcher
import requests
import urllib


def search_place(request):
    if request.method == 'POST':
        form = SearcherForm(request.POST)
        if form.is_valid():
            search = form.save()
            search.save()
            form = SearcherForm()
            searches = Searcher.objects.all()
            return render(request, 'client/search_place.html', context={'form': form,
                                                                        'searches': searches})
    else:
        form = SearcherForm()
        searches = Searcher.objects.all()
        return render(request, 'client/search_place.html', context={'form': form,
                                                                    'searches': searches})

def mahmut(request):
    location = request.GET.get("location")
    food = request.GET.get("food")
    if location == None and food == None:
        venue_info = []
        return render(request, "client/mahmut.html", context={"venue_info": venue_info, })

    else:
        parameters = {
            "near": location,
            "query": food,
            "limit": "10",
            "oauth_token": "0SEIPISC50KL3LM5EPQ1FABGRKB2MCODLQ4OAHDUJN3Y0L5D",
            "v": "20160816"
        }
        url_params = urllib.parse.urlencode(parameters)
        api_url = "https://api.foursquare.com/v2/venues/search?" + url_params
        print(api_url)
        response = requests.get(api_url) # 500 verirse ne oolur cevap vermezse ne olur
        response = response.json()
        print(response)
        venues = response["response"]["venues"]
        venue_info = []

        for venue in venues:
            venue_dict = {}
            venue_dict["name"] = venue.get("name", "---")
            venue_dict["phone"] = venue["contact"].get("formattedPhone", "---")
            venue_dict["usersCount"] = venue["stats"].get("usersCount", "---")
            venue_info.append(venue_dict)
        return render(request, "client/mahmut.html", context={"venue_info": venue_info, })









