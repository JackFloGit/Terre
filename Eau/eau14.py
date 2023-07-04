'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui trie les éléments donnés en argument 
par ordre ASCII.


Exemples d’utilisation :
$> python exo.py Alfred Momo Gilbert
Alfred Gilbert Momo


$> python exo.py A Z E R T Y
A E R T Y Z

Afficher error et quitter le programme en cas de problèmes d’arguments.


'''

import sys

#Functions
def ascii_sort(string_of_character):
    for index in range(0, (len(string_of_character)-1)):
        element_of_string = string_of_character[index]
        next_element_of_string = string_of_character[index + 1]
        if ord(element_of_string[0]) > ord(next_element_of_string[0]):
            string_of_character[index], string_of_character[index + 1] = string_of_character[index + 1], string_of_character[index]
    sorted_string = " ".join(string_of_character)
    return sorted_string

#Error_Management
if len(sys.argv[1:]) < 2:
    print("error")
    exit()

#Parsing
argument_of_command_line = sys.argv[1:]

#Problem_Solving
argument_sorted = ascii_sort(argument_of_command_line) 

#Display
print(argument_sorted)