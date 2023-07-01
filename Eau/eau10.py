'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui affiche le premier index d’un élément 
recherché dans un tableau. Le tableau est constitué de tous 
les arguments sauf le dernier. L’élément recherché est le dernier 
argument. Afficher -1 si l’élément n’est pas trouvé.

Exemples d’utilisation :
$> python exo.py Ceci est le monde qui contient Charlie 
un homme sympa Charlie
6


$> python exo.py test test test
0

$> python exo.py test boom
-1

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

#Functions
def search_element_in_list(list):
    search_word = list[-1]
    count = 0
    for word in list[0:-1]:
        count +=1
        if word == search_word:
            break
    if count == len(list[0:-1]):
        return "-1"
    return (count-1)

#Error_Management
if len(sys.argv[1:]) < 2:
    print("error")
    exit()

#Parsing
argument_list = sys.argv[1:]

#Problem_Solving
find_element = search_element_in_list(argument_list)

#Display
print(find_element)