import requests
import random

random_id = random.randint(1, 807)  # There are 807 Pokémon in the PokeAPI
url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

response = requests.get(url)

if response.status_code == 200:
  pokemon_data = response.json()

  print("Nom: ", pokemon_data['name'].capitalize())
  print("ID: ", pokemon_data['id'])
  print("Taille: ", pokemon_data['height'])
  print("Poids: ", pokemon_data['weight'])

  print("Image: ", pokemon_data['sprites']['front_default'])

  print("Compétences:")
  for competence in pokemon_data["abilities"]:
    print(competence['ability']['name'])
    print(competence['ability']['url'])
    print("/n")

else:
  print("Error: ", response.status_code)
