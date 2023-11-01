mon_tableau = [7, 19, 25, 3, 12, 40, 9]

# 1. comment obtenir le plus grand élément du tableau?

maximum = 0

for nombre in mon_tableau:
  if nombre > maximum:
    maximum = nombre

print(maximum)

# 2. comment multiplier tous les éléments entre eux?

total = 1

for nombre in mon_tableau:
  total = total * nombre

print(total)