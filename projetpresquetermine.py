from random import randint, seed

cartes = [0, "As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"]


def jeu(argent):
    score1, score2, carte_tire1, carte_tire2, nbcartes, nbcartesbanque = 0, 0, 0, 0, 0, 0
    print("Veuillez entrer votre mise (vous avez : ", argent, ")")
    mise = int(input())
    rejouer = 1
    while rejouer == 1:
        carte_tire1 = randint(1, 13)
        print("La carte tirée est :", cartes[carte_tire1])

        nbcartes += 1

        if carte_tire1 == 1:
            print("Vous avez tiré un as. Vous pouvez choisir sa valeur entre 1 et 11")
            valeur_as = int(input())
            score1 += valeur_as
        elif carte_tire1 > 10:
            score1 += 10
        else:
            score1 += carte_tire1

        if score1 > 21:
            print("Vous avez sauté")
            print("")
            rejeu(argent - mise)
            return
        print("Souhaitez-vous une carte ? (1: oui, 2: non)")
        rejouer = int(input())

    # la banque joue

    print("Vous avez obtenu :", score1, "points")
    print("La banque joue")

    while score2 < 17:
        carte_tire2 = randint(1, 13)
        print("La carte tirée est :", cartes[carte_tire2])

        nbcartesbanque += 1

        if carte_tire2 > 10:
            score2 += 10
        else:
            score2 += carte_tire2

    if score2 > 21:
        print("La banque a sauté")

    else:

        print("La banque a obtenu :", score2, "points")

        if score1 == score2:

            if score1 == 21:
                if nbcartes == 2 and nbcartesbanque != 2:
                    argent += mise
                    print("Vous avez gagne", mise)
                elif nbcartesbanque == 2 and nbcartes != 2:
                    print("La banque a gagné")
                else:
                    print("Égalité")
            else:
                print("Égalité")

        elif score1 > score2:
            argent += mise
            print("Vous avez gagné", mise)

        else:
            print("La banque a gagné")

    rejeu(argent)


def rejeu(argent):
    print("Souhaitez-vous jouer une autre partie ? (1: oui, 2: non) ")
    reponse = int(input())

    if reponse == 1:
        print("Vous venez de démarrer une nouvelle partie.")
        jeu(argent)
    else:
        print("Au revoir!")


print("Bienvenue au Blackjack")

argent = int(input("Veuillez entrer la quantité d'argent en votre possession : "))
graine = int(input("Entrez la graine : "))
seed(graine)
jeu(argent)
