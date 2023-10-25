
mon_tableau = [5, 11, 3, 18, 2]

# accès à un élément du tableau
ma_variable = mon_tableau[2]
print(ma_variable)


# accèes à un élément
print(mon_tableau[0])


# modification d'un élément
mon_tableau[2] = 6
print(mon_tableau)


# ajout d'un élément
mon_tableau.append(7)
print(mon_tableau)


# insertion d'un élément
mon_tableau.insert(3, 8)
print(mon_tableau)


# suppression d'un élément
mon_tableau.remove(11)
print(mon_tableau)


# vérifier qu'un élément existe
print(6 in mon_tableau)


# boucler sur un tableau
for nombre in mon_tableau:
    print(nombre)


# récupérer la taille d'un tableau
print(len(mon_tableau))

