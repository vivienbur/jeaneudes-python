import random

nombre_aleatoire = random.randint(1, 3)

for nombre_essais in range(10):
  
  nombre_saisi = int(input("Devine un nombre: "))

  if nombre_saisi < nombre_aleatoire:
    print("Plus grand")
  elif nombre_saisi > nombre_aleatoire:
    print("Plus petit")
  else:
    print("GAGNÉ!!! en " + str(nombre_essais + 1) + " essais")
    break


print("Perdu! Le nombre était: " + str(nombre_aleatoire))
