'''Créez un programme qui affiche ses arguments reçus
à l’envers.

Exemples d’utilisation :
$> python exo.py “Suis” “Je” “Drôle”
Drôle
Je
Suis


$> python exo.py ha ho
ho
ha

$> python exo.py “Bonjour 36”
Bonjour 36

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''


import sys

#Functions
def reverses_sequence(sequence_initiale):
    reversed = sequence_initiale[::-1]
    return reversed

#Error_Management
if not sys.argv[1:]:
    print("error")
    exit()

#Parsing
argument_command_line = sys.argv[1:]

#Problem_Solving
reversed_arguments = reverses_sequence(argument_command_line)
reversed_sequence = "\n".join(reversed_arguments)

#Display
print(reversed_sequence)