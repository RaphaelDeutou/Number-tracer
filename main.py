import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

num = "+REDACTED_PHONE_NUMBER"
monMum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monMum, "fr")
print(localisation)


operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))


clef = "REDACTED_API_KEY"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat,lng)


monMap = folium.Map(location=[lat,lng], zoom_start=12)
folium.Marker([lat,lng], popup=localisation).add_to(monMap)
monMap.save("map.html")

