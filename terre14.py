'''Créez un programme qui détermine si une liste d’entiers est triée ou pas.


 Exp :
       --> python script.py 9 8 3
           Pas triée !

       --> python script.py 3 8 9 12
           Triée !

       --> python script.py “Salut”
           erreur.'''


import sys


def lenght_argv():
    if len(sys.argv[1:]) < 2:
        print("erreur")
        exit()

def argument_is_integer_in_list():
    original_list = []
    original_list_copied = []
    for argument in sys.argv[1:]:
        if not argument.isdigit():
            print("erreur")
            exit()
        argument_integer = int(argument)
        original_list.append(argument_integer)
        original_list_copied.append(argument_integer)
    sorting_process(original_list, original_list_copied)


def sorting_process(original_list, original_list_copied):
    comparison_list = []
    while len(original_list_copied) != 0:
        index_sort = original_list_copied.index(min(original_list_copied))
        comparison_list.append(original_list_copied[index_sort])
        original_list_copied.pop(index_sort)
    print("Pas triée !") if original_list != comparison_list else print("Triée !")
    exit()

lenght_argv()
argument_is_integer_in_list()