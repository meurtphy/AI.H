import random

# Les gestes
gestes = {1: "ciseaux", 2: "pierre", 3: "feuille"}

# Fonction pour déterminer le gagnant
def determiner_gagnant(Kyle, T800):
    if Kyle == T800:
        return "egalite"
    elif (Kyle == 1 and T800 == 3) or (Kyle == 2 and T800 == 1) or (Kyle == 3 and T800 == 2):
        return "Kyle"
    else:
        return "T800"
print("Bienvenue dans la Resistance ! Pierre (2), Feuille (3), Ciseaux (1)")

while True:
    try:
        # Le T800 choisit un nombre aleatoire entre 1, 2, 3 grace a random...
        geste_T800 = random.randint(1, 3)
        # Kyle reese choisit un geste(parle a ma main!!)
        geste_Kyle = int(input("Entrez votre choix (1 pour ciseaux, 2 pour pierre, 3 pour feuille) : "))

        if geste_Kyle not in gestes:
            print("C est pas complique choisit entre 1, 2 et 3 foutu humain!!!!")
            continue

        print(f"Kyle reese a choisi : {gestes[geste_Kyle]}")
        print(f"T800 a choisi : {gestes[geste_T800]}")

        # le gagnant est ...(resultat)
        gagnant = determiner_gagnant(geste_Kyle, geste_T800)
        if gagnant == "egalite":
            print("Je reviendrais")
        elif gagnant == "Kyle":
            print("Hasta la vista Baby!!")
        else:
            print("You are a looser bouuuuh (sarah is dead)!!!")
    except ValueError:
            print("Suis les regle, si tu veux vivre.")