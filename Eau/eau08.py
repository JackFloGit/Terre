'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui détermine si une chaîne de caractères 
ne contient que des chiffres.


Exemples d’utilisation :
$> python exo.py “4445353”
true


$> python exo.py 42
true

$> python exo.py “Bonjour 36”
false

Afficher error et quitter le programme en cas 
de problèmes d’arguments.

'''

import sys

#Functions
def check_all_is_figure(string):
    for index in range(len(string)):
        if ord(string[index]) < 48 or ord(string[index]) > 57:
            return False
        return True
#Error_Management
if len(sys.argv[1:])!= 1:
    print("error")
    exit()

#Parsing
string_of_figure = sys.argv[1]

#Problem_Solving
all_is_figure = check_all_is_figure(string_of_figure)

#Display
print("true") if all_is_figure else print("false")