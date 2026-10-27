import os

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
from dotenv import load_dotenv

load_dotenv()

NUMBER_TO_TRACE = os.environ["NUMBER_TO_TRACE"]
OPENCAGE_API_KEY = os.environ["OPENCAGE_API_KEY"]

monMum = phonenumbers.parse(NUMBER_TO_TRACE)
localisation = geocoder.description_for_number(monMum, "fr")
print(localisation)


operateur = phonenumbers.parse(NUMBER_TO_TRACE)
print(carrier.name_for_number(operateur, "fr"))


coord = OpenCageGeocode(OPENCAGE_API_KEY)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat,lng)


monMap = folium.Map(location=[lat,lng], zoom_start=12)
folium.Marker([lat,lng], popup=localisation).add_to(monMap)
monMap.save("map.html")
