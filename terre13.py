'''Créez un programme qui prend en paramètre trois entiers
et affiche la valeur du milieu.

   exp :
           --> python script.py 11 40 34
               34
           --> python script.py 2 1 3
               2
           --> python script.py 2 2 2
               erreur.'''


import sys


def lenght_argv():
    if len(sys.argv[1:]) != 3:
        print("erreur")
        exit() 


def format_each_arguments():
    first_argument = (sys.argv[1]).isdigit()
    second_argument = (sys.argv[2]).isdigit()
    third_argument = (sys.argv[3]).isdigit()
    if not first_argument or not second_argument or not third_argument:
        print("erreur")
        exit()
    first_integer = int(sys.argv[1])
    second_integer = int(sys.argv[2])
    third_integer = int(sys.argv[3])
    sorting_rules(first_integer, second_integer, third_integer)


def sorting_rules(first_integer, second_integer, third_integer):
    if first_integer == second_integer or first_integer == third_integer or second_integer == third_integer:
        print("erreur")
        exit()
    middle_list=[]
    middle_list.append(first_integer)
    if (second_integer) < (middle_list[0]):
        middle_list.insert(0,first_integer)
    else:
        middle_list.append(second_integer)
    if (third_integer) < (middle_list[0]):
        middle_list.insert(0,third_integer)
    elif (third_integer) < (middle_list[1]):
        middle_list.insert(1,third_integer)
    else:
        middle_list.append(third_integer)
    print(middle_list[1])

lenght_argv()
format_each_arguments()