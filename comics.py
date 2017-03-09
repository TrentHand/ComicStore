import os
import json

#this is looping through all the comics in comics.json, creating each one as an object called complete_comic and appending them into a list called all_comics.
def parseComics():
    all_comics = []
    complete_comic = {}

    try:
        with open("comics.json", "r") as files:
            comic_data = json.load(files)
            comics = comic_data["results"]
            # print(comics)
            for comic in comics:
                complete_comic = {
                    'comic_id':comic["id"],
                    'comic_title':comic["title"],
                    'description':comic["description"],
                    'price':comic["prices"][0]["price"],
                    'comic_cover':comic["thumbnail"]["path"] + "." + comic["thumbnail"]["extension"]
                }
                all_comics.append(complete_comic)

    except: 
        pass 

parseComics()




