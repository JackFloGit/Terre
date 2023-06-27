'''Créez un programme qui affiche le N-ème élément de la célèbre
suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite 
et le premier élément étant à l’index 0.

Exemples d’utilisation :
$> python exo.py 3
2
$>

Afficher -1 si le paramètre est négatif ou mauvais.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 418
'''

import sys


#Functions
def generate_sequence_fibonacci_until_n(n):
    if n == "0":
        return 0
    elif n == "1":
        return 1
    elif n == "2":
        return 1
    else:
        count = 0
        first_number = 0
        second_number = 1
        while count != (int(n)-2):
            calcul_sequence = first_number + second_number
            first_number = second_number
            second_number = calcul_sequence
            count += 1
        return calcul_sequence


#Error_Management
if not len(sys.argv[1:]):
    print("error")
    exit()
check_arguments_is_digit = sys.argv[1].isdigit()
if not check_arguments_is_digit:
    print("error")
    exit()

#Parsing
element_number = sys.argv[1]

#Problem_Solving
number_Fibonacci_sequence = generate_sequence_fibonacci_until_n(element_number)

#Display
print(number_Fibonacci_sequence)