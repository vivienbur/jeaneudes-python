
fruits = ["babane", "poire", "pomme"]
print(fruits)

# accès à un élément du tableau
mon_fruit = fruits[2]
print(mon_fruit) 


# accèes à un élément
print(fruits[0])


# modification d'un élément
fruits[2] = "framboise"
print(fruits)


# ajout d'un élément
fruits.append("citron")
print(fruits)


# insertion d'un élément
fruits.insert(3, "cerise")
print(fruits)


# suppression d'un élément
fruits.remove("citron")
print(fruits)


# vérifier qu'un élément existe
print("carotte" in fruits)
print("framboise" in fruits)


# boucler sur un tableau
for un_fruit in fruits:
    print(un_fruit)


# récupérer la taille d'un tableau
print(len(fruits))

