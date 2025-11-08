"""Create a Mastermind Game"""

import random

def generate_random_number():
    """Function to generate a random number with contraints: 11111 < random < 99999"""
    random_number = random.randint(1, 99999)

    while len(str(random_number)) < 5:
        generate_random_number()

    return str(random_number)


def game():
    """The core function of the mastermind simulation game"""
    remain = 10
    random_number = generate_random_number()

    while remain > 0:
        combinaison = str(input("Entrer votre combinaison (5 chiffres compris entre 1 et 9) :  "))
        
        while len(combinaison) < 5 or len(combinaison) > 5:
            #print("isDigit", combinaison.isdigit)
            combinaison = str(input("Combinaison invalide, réessayez (5 chiffres compris entre 1 et 9):  "))
            
        good_placed = 0

        print("Random", random_number, "and remain", remain)

        remain = remain - 1
        c1 = combinaison[0]
        c2 = combinaison[1]
        c3 = combinaison[2]
        c4 = combinaison[3]
        c5 = combinaison[4]

        r1 = random_number[0]
        r2 = random_number[1]
        r3 = random_number[2]
        r4 = random_number[3]
        r5 = random_number[4]

        if c1 == r1:
            good_placed = good_placed + 1

        if c2 == r2:
            good_placed = good_placed + 1

        if c3 == r3:
            good_placed = good_placed + 1

        if c4 == r4:
            good_placed = good_placed + 1

        if c5 == r5:
            good_placed = good_placed + 1

        if good_placed == 5:
            return print(f"Bravo ! Vous aviez gagné après {10-remain} essais")
        else:
            print(good_placed, " numéros biens placés. Réessayez !")


game()
