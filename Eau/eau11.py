'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui affiche la différence minimum absolue 
entre deux éléments d’un tableau constitué uniquement de nombres. 
Nombres négatifs acceptés.

Exemples d’utilisation :
$> python exo.py 5 1 19 21
2

$> python exo.py 20 5 1 19 21
1

$> python exo.py -8 -6 4
2

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

#Functions
def get_absolute_value(sequence):
    list_value=[]
    level = 0
    while level != (len(sequence)):
        index = 0
        while index < len(sequence):
            if (int(sequence[level])) != (int(sequence[index])):
                substraction_value = (int(sequence[level])) - (int(sequence[index]))
                if substraction_value < 0:
                    substraction_value *= -1
                list_value.append(substraction_value)
            index += 1
        level +=1
    smallest_value = min(list_value)
    return smallest_value

#Error_Management
if len(sys.argv[1:]) < 2:
    print("error")
    exit()

for character in sys.argv[1:]:
    character_replace = character.replace('-','')
    if not character_replace.isdigit():
        print("error")
        exit()

#Parsing
sequence_list = sys.argv[1:]

#Problem_Solving
absolute_value = get_absolute_value(sequence_list)

#Display
print(absolute_value)