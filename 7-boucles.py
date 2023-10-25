# For loop
for i in range(5):
    print(i)


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
    x += 1


# boucler sur un tableau
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)