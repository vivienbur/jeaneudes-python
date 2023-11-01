import random

# on prend un nombre aléatoire entre 1 et 100
nombre_aleatoire = random.randint(1, 5)

nombre_essais = 0

# le joueur a 10 essais pour trouver le nombre aléatoire
for nombre_essais in range(1, 4):

  nombre_saisi = int(input("Devine un nombre: "))

  if nombre_saisi < nombre_aleatoire:
    print("Plus grand")
  elif nombre_saisi > nombre_aleatoire:
    print("Plus petit")
  else:
    print("GAGNÉ!!!")
    print("En " + str(nombre_essais) + " essais")
    break

# comment afficher le nombre aléatoire quand on a perdu?
if(nombre_essais == 3):
  print("PERDU!!!")
  print("Le nombre était " + str(nombre_aleatoire))