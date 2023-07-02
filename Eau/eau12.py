'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui trie une liste de nombres. Votre programme 
devra implémenter l’algorithme du tri à bulle.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_bubble_sort(array) {
	# votre algorithme
	return (new_array)
}

Exemples d’utilisation :
$> python exo.py 6 5 4 3 2 1
1 2 3 4 5 6

$> python exo.py test test test
error

Afficher error et quitter le programme en cas de problèmes d’arguments.

Wikipedia vous présentera une belle description de cet algorithme de tri.
'''

import sys

#Functions
def my_bubble_sort(list):
    counter = 0
    while counter != (len(list)-1):
        index = 0
        while index < (len(list)-1):
            comparison = list[index] > list[index + 1]
            if comparison:
                list[index], list[index+1] = list[index+1], list[index]
            index += 1
        counter += 1
    new_list = " ".join(list)
    return new_list


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
argument_sequence = sys.argv[1:]

#Problem_Solving
sorted_list = my_bubble_sort(argument_sequence)

#Display
print (sorted_list)