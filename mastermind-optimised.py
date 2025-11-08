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
        
        # Use for loop to optimise commbinaison checking
        for i in range((5)):
            #print(i)
            if combinaison[i] == random_number[i]:
                good_placed = good_placed + 1
       

        if good_placed == 5:
            return print(f"Bravo ! Vous aviez gagné après {10-remain} essais")
        else:
            print(good_placed, " numéro(s) bien(s) placé(s). Réessayez !")


game()
