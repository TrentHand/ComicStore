import os
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView

#this is looping through all the comics in comics.json, creating each one as an object called complete_comic and appending them into a list called all_comics.
class ComicsView(TemplateView):
    template_name = '/src/profiles/templates/home.html'

def parseComics(request):
    all_comics = []
    complete_comic = {}

    try:
        with open("../comics.json", "r") as files:
            comic_data = json.load(files)
            comics = comic_data["results"]
            for comic in comics:
                complete_comic = {
                    'comic_id':comic["id"],
                    'comic_title':comic["title"],
                    'description':comic["description"],
                    'price':comic["prices"][0]["price"],
                    'comic_cover':comic["thumbnail"]["path"] + "." + comic["thumbnail"]["extension"]
                }
                all_comics.append(complete_comic)
                print(complete_comic)

    except: 
        print("HAPPPPPPYYPYPPPYY") 

    return render(request, '../templates/home.html', {'all_comics':all_comics})






