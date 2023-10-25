mon_tableau = [5, 11, 3, 18, 2]

# Accessing elements in a list
ma_variable = mon_tableau[2]
print(ma_variable)

# Accessing elements in a list
print(mon_tableau[0])

# Modifying elements in a list
mon_tableau[2] = 6
print(mon_tableau)

# Appending elements to a list
mon_tableau.append(7)
print(mon_tableau)

# Inserting elements at a specific position in a list
mon_tableau.insert(3, 8)
print(mon_tableau)

# Removing elements from a list
mon_tableau.remove(11)
print(mon_tableau)

# Checking if an element exists in a list
print(6 in mon_tableau)

# Looping through a list
for nombre in mon_tableau:
    print(nombre)

# Getting the length of a list
print(len(mon_tableau))