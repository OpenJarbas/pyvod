from pyvod.db import add_movie
import requests
from pprint import pprint
import bs4
import internetarchive as ia

from internetarchive import get_item
from internetarchive import ArchiveSession

VALID_FORMATS = ['MPEG2', "Ogg Video", "512Kb MPEG4"]

from os.path import exists

if exists("seen.txt"):
    with open("seen.txt") as f:
        seen = f.read().split("\n")
else:
    seen = []


def parse_collection(collection_name):
    global seen
    session = ArchiveSession()

    entries = list(ia.Search(session, 'collection:' + collection_name))
    for idx, entry in enumerate(entries):

        item_id = entry['identifier']
        if item_id in seen:
            continue
        seen.append(item_id)
        item = get_item(item_id)
        meta = requests.get(item.urls.metadata).json()

        tags = []
        if meta["metadata"].get('subject'):
            if isinstance(meta["metadata"]["subject"], str):
                tags += meta["metadata"]["subject"].split(";")
            if isinstance(meta["metadata"]["subject"], list):
                tags += meta["metadata"]["subject"]
        description = meta["metadata"].get('description')
        if description:
            try:
                description = bs4.BeautifulSoup(description,
                                                "html.parser").text
            except:
                pass
        movie = {
            "identifier": item_id,
            "collection": meta["metadata"]["collection"],
            "tags": tags,
            "streams": [],
            "title": meta["metadata"]["title"],
            "runtime": meta["metadata"].get('runtime'),
            'mediatype': meta["metadata"]['mediatype'],
            'description': description,
            'license': meta["metadata"].get('licenseurl'),
            "sound": meta["metadata"].get("sound"),
            "color": meta["metadata"].get("color"),
            "reviews": meta["metadata"].get("revies", [])
        }

        #        movie["reviews"] = meta['reviews']

        for f in meta["files"]:
            if f["format"] in VALID_FORMATS:
                stream = item.urls.download + "/" + f["name"]
                movie["streams"].append(stream)

        yield movie
        with open("seen.txt", "w") as f:
            f.write("\n".join(seen))


collections = [
    "cinemocracy",
    "SciFi_Horror",
    "feature_films_picfixer",
    "TheVideoCellarCollection",
    "feature_films",

    "movie_trailers",

    "silenthalloffame",
    "Comedy_Films",
    "Film_Noir",
    "short_films",
    "movie_trailers_picfixer",
    "nuraypictures",
    "movie_trailers",
    "sinema-trailers",
    "stock_footage",
"moviesandfilms",
]

for collection_name in collections:
    print(collection_name)
    for movie in parse_collection(collection_name):
        add_movie(movie, db_path="pyvod/res/" + collection_name + ".jsondb")

        print(len(seen), movie["title"])
        # print(movie)
