# For loop
for num in range(5):
    print(num)


for num in range(1, 6):
    print(num)


# boucle avec étapes
for num in range(3, 13, 2):
    print(num)


# briser l'exécution d'une boucle
for i in range(10):
    if i == 5:
        break
    print(i)


# While loop
x = 0
while x < 5:
    print(x)
    x = x + 1


# boucler sur un tableau
mon_tableau = [7, 12, 5, 24, 9]
for element in mon_tableau:
    print(element)