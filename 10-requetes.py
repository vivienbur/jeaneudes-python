import requests

url = "https://v2.jokeapi.dev/joke/Any?lang=fr"

response = requests.get(url)

if response.status_code == 200:

  blague = response.json()

  print("Question: ", blague['setup'])
  print("Réponse: ", blague['delivery'])

else:
  print("Error: ", response.status_code)
