'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display
Créez un programme qui affiche le premier nombre premier supérieur 
au nombre donné en argument.

Exemples d’utilisation :
$> python exo.py 14
17
$>

Afficher -1 si le paramètre est négatif ou mauvais.
'''

import sys

#Functions
def is_prime(number):
    if number < 2:
        return False
    for y in range(2,int((number**0.5)+1)):
        if number % y == 0:
            return False
    return True

def generate_prime_greater_than_x(x):
    x = int(x)
    while True:
        x += 1
        if is_prime(x):
            return x

#Error_Management
if len(sys.argv[1:]) != 1:
    print("-1")
    exit()

check_argument_is_digit = sys.argv[1].isdigit()

if not check_argument_is_digit:
    print("-1")
    exit()
#Parsing
number_argument = int(sys.argv[1])

#Problem_Solving
prime_number = generate_prime_greater_than_x(number_argument)

#Display
print(prime_number)