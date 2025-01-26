import random

# L'ordinateur choisit un nombre
nombre_secret = random.randint(1, 10)

print("Bienvenue au jeu de devinette ! Devinez un nombre entre 1 et 10.")

# Boucle pour deviner
while True:
    devine = int(input("Entrez votre nombre : "))

    if devine < nombre_secret:
        print("Trop petit !")
    elif devine > nombre_secret:
        print("Trop grand !")
    else:
        print("Bravo ! Vous avez deviné.")
        break
