'''Créez un programme qui affiche si un nombre est 
premier ou pas.
 
 exp :
       --> script.py 5
           Oui, 5 est un nombre premier.

       --> script.py 6  
           Non, 6 n'est pas un nombre premier.

!! 0 et 1 ne sont pas des nombres premiers (gerer erreur)!!'''


import sys 


def lenght_argv():
    if len(sys.argv[1:]) !=1:
        print("erreur")
        exit()


def check_is_number():
    argument = sys.argv[1]
    number = argument.isdigit()
    if number == False:
        print ("erreur")
        exit()
    else:
        x = int(argument)
    display_if_prime(x, argument)


def display_if_prime(x, argument):
    '''Check if is prime in sequence from 2 to square root of number.
    
    first step: define square root of number.
    second step: create sequence from 2 to square root.
    third step: modulo the number with the sequence.
    last step: compare with 0.'''
    square_root_x = (x)**(0.5)
    to_integer_square_root_x = int(square_root_x)
    if to_integer_square_root_x > 1 and to_integer_square_root_x < 2:
        print("Oui,",argument,"est un nombre premier 1.")
        exit()

    sequence = range(2, ((to_integer_square_root_x)+1))
    results = []

    for y in sequence:
        modulo = (x)%(y)
        results.append(modulo)

    premier = True

    for r in results:
        if r == 0:
            premier = False
    print("Non,",argument,"n'est pas un nombre premier.") if not premier else print("Oui,",argument,"est un nombre premier.")

lenght_argv()
check_is_number()