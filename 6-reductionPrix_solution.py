# on saisit le prix puis on convertit le texte en nombre
prix_texte = input("Quel est le prix de votre article?: ")
prix_nombre = int(prix_texte)

# on saisit la quantité en faisant la conversion texte->nombre en même temps
quantite = int(input("Combien d'articles allez-vous acheter?: "))

if quantite > 10:
  total = prix_nombre * quantite * 0.9
else:
  total = prix_nombre * quantite

print("Voici le prix total:", total)
