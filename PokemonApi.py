#PokemonApi

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code ==200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrive data {response.status_code}")

pokemon_name = "ditto"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
    print(f"Base Experience: {pokemon_info["base_experience"]}")