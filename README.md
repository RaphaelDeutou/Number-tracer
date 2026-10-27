# Number-tracer

Petit script Python qui géolocalise approximativement un numéro de téléphone et affiche l'opérateur associé, puis place le résultat sur une carte interactive.

## Fonctionnement

1. `phonenumbers` identifie la région et l'opérateur à partir du numéro
2. [OpenCage Geocoding API](https://opencagedata.com/) convertit la localisation en coordonnées GPS
3. `folium` génère une carte HTML (`map.html`) centrée sur ces coordonnées

## Prérequis

`pip install phonenumbers opencage folium python-dotenv`

Une clé API OpenCage est nécessaire (gratuite sur opencagedata.com). Copier `.env.example` vers `.env` et y renseigner `NUMBER_TO_TRACE` et `OPENCAGE_API_KEY`.

## Statut

Script d'expérimentation personnel autour des API de géolocalisation.
