import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

num = "+4915906724613"
monMum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monMum, "fr")
print(localisation)


operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))


clef = "53603973bc9e40298e67fe27ff4db114"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat,lng)


monMap = folium.Map(location=[lat,lng], zoom_start=12)
folium.Marker([lat,lng], popup=localisation).add_to(monMap)
monMap.save("map.html")

