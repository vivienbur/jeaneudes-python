# exemple de condition avec if-else
# bien regarder la syntaxe!! (ex: ne pas oublier les deux points)
prix_glace = 5

argent_texte = input("Combien d'argent as-tu dans ton portefeuille?: ")
argent_nombre = int(argent_texte)

if (argent_nombre >= prix_glace):
  print("Tu peux acheter ta glace!! :)")
else:
  print("Tu n'as pas assez d'argent pour acheter ta glace :(")


