import os
import json


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




