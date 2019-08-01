import requests
import matplotlib.pyplot as plt 
import json

url = 'https://pokeapi.co/api/v2/pokemon/?offset=20&limit=964'
response = requests.get(url)
data = response.text 
parsed_data = json.loads(data)

results = parsed_data['results']
names = []
pokemon_json = []
pokemons  = []

i = 0
while i < 10:
    names.append(results[i]['name'])
    pokemon_json.append(results[i]['url'])
    i = i + 1

for url in pokemon_json:
    response = requests.get(url)
    pokemons.append(json.loads(response.text))

pokemon_heights = []


for pokemon in pokemons:
    pokemon_data = []
    pokemon_data.append(pokemon['height'])
    pokemon_data.append(pokemon['types'][0]['type']['name'])
    pokemon_heights.append(pokemon_data)

pokemon_heights.sort()
print(pokemon_heights)