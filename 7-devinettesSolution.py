import random

nombre_aleatoire = random.randint(1, 100)
essais = 0

while essais < 10:

  nombre_saisi = int(input("Devine un nombre: "))
  essais = essais + 1
  
  if nombre_saisi < nombre_aleatoire:
    print("Plus grand")
  elif nombre_saisi > nombre_aleatoire:
    print("Plus petit")
  else:
    print("GAGNÉ!!! en " + str(essais) + " essais")
    break

if essais == 10:
  print("Perdu! Le nombre était: " + str(nombre_aleatoire))
