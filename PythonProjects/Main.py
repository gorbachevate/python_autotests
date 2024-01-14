import requests

token = "9ca283e5fb6e90d193c341110a5f8cb5"

response = requests.post("https://api.pokemonbattle.me:9104/pokemons", json= {
    "name": "Булька",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    }, headers= {"trainer_token":token,
                 "Content-Type":"application/json"})

print(response.text)

response = requests.put("https://api.pokemonbattle.me:9104/pokemons", json= {
    "name": "Meoww",
    "pokemon_id": "27269",
    "photo": "https://dolnikov.ru/pokemons/albums/052.png"
    }, headers= {"trainer_token": token,
                 "Content-Type":"application/json"})

print(response.text)

response = requests.post("https://api.pokemonbattle.me:9104/trainers/add_pokeball", json= {
    "pokemon_id": "27269"
    }, headers= {"trainer_token": token,
                 "Content-Type":"application/json"})

print(response.text)