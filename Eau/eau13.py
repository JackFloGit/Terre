'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui trie une liste de nombres. Votre programme 
devra implémenter l’algorithme du tri par sélection.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_select_sort(array) {
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
def my_select_sort(list):
    for first_index in range(0, (len(list)-1)):
        lowest_rank = int(list[(first_index)])
        index_lowest_rank = first_index
        for second_index in range((first_index) + 1, len(list)):
            if int(list[second_index]) < int(lowest_rank):
                lowest_rank = int(list[second_index])
                index_lowest_rank = int(second_index)
        storage_variable = list[first_index]
        list[first_index] = str(lowest_rank)
        list[index_lowest_rank] = storage_variable
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
sorted_list = my_select_sort(argument_sequence)

#Display
print(sorted_list)