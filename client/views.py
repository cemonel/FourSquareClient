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
            venue_dict["venue_id"] = venue.get("id", "---")
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
                                                          "previous_searches": previous_searches,
                                                          })


def venue_detail(request, venue_id):
    parameters = {"sort": "recent",
                  "oauth_token": "0SEIPISC50KL3LM5EPQ1FABGRKB2MCODLQ4OAHDUJN3Y0L5D",
                  "v": "20160821",
                  "limit": "10",
                  }
    api_url = urllib.parse.urlencode(parameters)
    api_url = "https://api.foursquare.com/v2/venues/%s/tips?" % venue_id + api_url
    response = requests.get(api_url)
    response = response.json()
    tips = response["response"]["tips"]["items"]
    tips_info = []

    for tip in tips:
        tip_dict = {}
        user_photo = tip["user"]["photo"].get("suffix", "---")
        user_photo = "https://irs3.4sqi.net/img/user/" + "200x200" + user_photo
        tip_dict["user_photo"] = user_photo
        tip_dict["tip_text"] = tip.get("text", "---")
        tip_dict["user_name"] = tip["user"].get("firstName", "---")
        tip_dict["user_last_name"] = tip["user"].get("lastName", "")
        tips_info.append(tip_dict)

    return render(request, "client/venue_detail.html", context={"venue_id": venue_id,
                                                                "tips_info": tips_info,
                                                                })







