'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui affiche toutes les valeurs comprises 
entre deux nombres dans l’ordre croissant. Min inclus, max exclus.

Exemples d’utilisation :
$> python exo.py 20 25
20 21 22 23 24

$> python exo.py 25 20
20 21 22 23 24

$> python exo.py hello
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

#Functions
def generate__sequence_between_two_numbers(first_number, second_number):
    check = (int(first_number)) < (int(second_number))
    if check:
        small_number = int(first_number)
        large_number = int(second_number)
    else:
        small_number = int(second_number)
        large_number = int(first_number)
    growing_numbers_list = []
    growing_numbers_list.append(str(small_number))
    while small_number != ((large_number)-1):
        small_number += 1
        growing_numbers_list.append(str(small_number))
        sequence = " ".join(growing_numbers_list) 
    return sequence

#Error_Management
if len(sys.argv[1:]) != 2:
    print("error")
    exit()
character = (sys.argv[1] + sys.argv[2]).isdigit()
if not character:
    print("error")
    exit()

#Parsing
first_argument_number = sys.argv[1]
second_argument_number = sys.argv[2]

#Problem_Solving
growing_sequence = generate__sequence_between_two_numbers(first_argument_number, second_argument_number)

#Display
print(growing_sequence)