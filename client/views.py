from django.shortcuts import render
from .forms import SearcherForm
from .models import Searcher
import requests
import urllib


def search(request):
    form = SearcherForm(request.GET)
    if form.is_valid():
        location = form.instance.location
        food = form.instance.food
        search = form.save()
        search.save()
        form = SearcherForm()
        previous_searches = Searcher.objects.order_by('-id')[:5]
        parameters = {
            "near": location,
            "query": food,
            "limit": "10",
            "oauth_token": "0SEIPISC50KL3LM5EPQ1FABGRKB2MCODLQ4OAHDUJN3Y0L5D",
            "v": "20160816"
        }
        url_params = urllib.parse.urlencode(parameters)
        api_url = "https://api.foursquare.com/v2/venues/search?" + url_params
        response = requests.get(api_url)# 500 verirse ne oolur cevap vermezse ne olur
        response = response.json()
        venues = response["response"]["venues"]
        venue_info = []

        for venue in venues:
            venue_dict = {}
            venue_dict["name"] = venue.get("name", "---")
            venue_dict["phone"] = venue["contact"].get("formattedPhone", "---")
            venue_dict["usersCount"] = venue["stats"].get("usersCount", "---")
            venue_info.append(venue_dict)

    else:
        form = SearcherForm()
        previous_searches = Searcher.objects.order_by('-id')[:5]
        venue_info = []
    return render(request, "client/search.html", context={"venue_info": venue_info,
                                                          "form": form,
                                                          "previous_searches": previous_searches, })










