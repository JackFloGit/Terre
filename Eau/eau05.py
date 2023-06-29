'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.

Exemples d’utilisation :
$> python exo.py bonjour jour
true

$> python exo.py bonjour joure
false

$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

#Functions

def index_each_value(first_string, second_string):
    sequence = 0
    index_list = []
    for sequence in range(len(first_string)):
        if (first_string[sequence]) == (second_string[0]):
            index_list.append(sequence)
    return index_list

def compares_the_elements(first_word, second_word,list_of_index):
    index = 0
    while index != len(list_of_index):
        for number in range(0, len(second_word)):
            if list_of_index[index] + number >= len(first_word):
                break
            if first_word[(list_of_index[index]) + number] != second_word[number]:
              break 
        else:
            return True
        index +=1
    return False                

#Error_Management
if len(sys.argv[1:]) != 2:
    print("error")
    exit()


is_first_element_digit = (sys.argv[1]).isdigit()
is_second_element_digit = (sys.argv[2]).isdigit()
if is_first_element_digit or is_second_element_digit:
    print("error")
    exit()

#Parsing
first_argument_string = sys.argv[1]
second_argument_string = sys.argv[2]

#Problem_Solving
index_each_letters = index_each_value(first_argument_string,second_argument_string)
compared = compares_the_elements(first_argument_string,second_argument_string,index_each_letters)

#Display
print(compared)