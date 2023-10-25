import random

# on prend un nombre aléatoire entre 1 et 100
nombre_aleatoire = random.randint(1, 100)

# le joueur a 10 essais pour trouver le nombre aléatoire
for nombre_essais in range(10):

  nombre_saisi = int(input("Devine un nombre: "))

  if nombre_saisi < nombre_aleatoire:
    print("Plus grand")
  elif nombre_saisi > nombre_aleatoire:
    print("Plus petit")
  else:
    print("GAGNÉ!!! en " + str(nombre_essais + 1) + " essais")
    break

# comment afficher le nombre aléatoire quand on a perdu?
