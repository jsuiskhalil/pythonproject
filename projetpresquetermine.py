from random import randint, seed

print("Bienvenue au Blackjack")
graine = int(input("Entrez la graine : "))
seed(graine)
score1 = 0
score2 = 0
carte_tire1 = 0
carte_tire2 = 0

if carte_tire1 == 11 == "Jamila":
    print("Jamila")

argent = int(input("Veuillez entrer la quantité d'argent en votre possession : "))

print("Veuillez entrer votre mise (vous avez : ", argent)
portefeuille = int(input())

if score1 < 21:
    carte_tire1 = randint(1, 13)
    print("la carte tirée est : ", carte_tire1)
    score1 += carte_tire1
    print(score1)
    print("Souhaitez-vous une carte ? (1: oui, 2: non")
    encorejouer = int(input())

elif score1 > 21:
    print("vous avez sauté")

while encorejouer == 1:
    carte_tire1 = randint(1, 13)
    print("la carte tirée est : ", carte_tire1)
    score1 += carte_tire1
    print("Souhaitez-vous une carte ? (1: oui, 2: non")
    encorejouer = int(input())
    if encorejouer == 2:
        print("vous avez obtenu : ", score1)
    if score1 > 21:
        print("vous avez sauté")
    if encorejouer == 1:
        print("la banque joue :")

argent2 = int(input("Veuillez entrer la quantité d'argent en votre possession : "))

print("Veuillez entrer votre mise (vous avez : ", argent2)
portefeuille2 = int(input())

if score2 < 21:
    carte_tire2 = randint(1, 13)
    print("la carte tirée est : ", carte_tire2)
    score2 += carte_tire2
    print(score2)
    print("Souhaitez-vous une carte ? (1: oui, 2: non")
    encorejouer = int(input())

while encorejouer == 1:
    carte_tire2 = randint(1, 13)
    print("la carte tirée est : ", carte_tire2)
    score2 += carte_tire2
    print("Souhaitez-vous une carte ? (1: oui, 2: non")
    encorejouer = int(input())
    if encorejouer == 2:
        print("la banque a obtenu : ", score2)

    if score1 == score2:
        print("Égalité")

    elif score1 > score2 and score1 <= 21:
        print("vous avez gagné")

    else:
        print("la banque a gagné")

"""

print("Vous avez sauté")
print("Souhaitez-vous une carte ? (1: oui, 2: non ")
print("Vous avez obtenu ")
print("points")
print("La banque joue :")
print("La carte tirée est : ")
print("La banque a sauté")
print("Vous gagnez")
print("La banque a obtenu ")
print(" points")
print("La banque gagne")
print("Égalité")
print("Vous gagnez ")
print("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) ")"""
