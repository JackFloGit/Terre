'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.

Exemples d’utilisation :
$> python exo.py “Hello world !”
HeLlO wOrLd !

$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments. 
'''

import sys

#Functions
def upper_one_out_of_two(string):
    index_list = []
    index = 0
    for index in range(0, (len(string)), 2):
            if (ord(string[index])) < 65 or (ord(string[index])) > 90 and (ord(string[index])) < 97 or (ord(string[index])) > 122:
                index += 1
            index_list.append(index)
    for i in index_list:
        string = string[:i] + string[i].upper() + string[i+1:]
    return string

#Error_Management
if len(sys.argv[1:]) != 1 :
    print("error 1")
    exit()
for character in sys.argv[1]:
    if character > chr(48) and character < chr(57):
        print("error")
        exit()


#Parsing
argument_string = sys.argv[1]

#Problem_Solving
new_string = upper_one_out_of_two(argument_string)

#Display
print(new_string)