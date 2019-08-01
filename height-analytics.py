import requests
import matplotlib.pyplot as plt 
import json

url = 'https://pokeapi.co/api/v2/pokemon/?offset=20&limit=964'
response = requests.get(url)
data = response.text 
parsed_data = json.loads(data)

results = parsed_data['results']
names = []
jsons = []
pokemons  = []

i = 0
while i < 100:
    names.append(results[i]['name'])
    jsons.append(results[i]['url'])
    i = i + 1

for url in jsons:
    response = requests.get(url)
    pokemons.append(json.loads(response.text))

heights = []

for pokemon in pokemons:
    pokemon_data = []
    pokemon_data.append(pokemon['height'])
    pokemon_data.append(pokemon['name'])
    heights.append(pokemon_data)

heights.sort()

print(heights)