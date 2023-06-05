""" Créez un programme qui affiche le résultat d’une puissance.
L’exposant ne pourra pas être négatif.

    exp:
    --> python exo.py 2 3
        8

   !! gérer les potentielles erreurs d’arguments. !!
"""

import sys


def lenght_argv():
    if len(sys.argv[1:]) != 2:
        print ("erreur")
        exit ()


def is_number_check():
    '''check if the arguments are number.'''

    first_argument = sys.argv[1]
    first_argument_replace = first_argument.replace("-","").replace(".","").replace(",","")

    second_argument = sys.argv[2]
    second_argument_replace = second_argument.replace("-","").replace(".","").replace(",","")
    
    isdigit_first_arg = first_argument_replace.isdigit()
    isdigit_second_arg = second_argument_replace.isdigit()
    
    if not isdigit_first_arg or not isdigit_second_arg:
        print ("erreur")
        exit()
    decimal_point_management(first_argument, second_argument)

def decimal_point_management(first_argument, second_argument):
    '''This function manage the coma and the point.'''

    first_argv_point= first_argument.replace(",",".")
    first_count_point = first_argv_point.count(".")
    
    second_argv_point = second_argument.replace(",",".")
    second_count_point = second_argv_point.count(".")
    
    if first_count_point > 1 or second_count_point > 1:
        print ("erreur")
        exit()
    define_type(first_argv_point, second_argv_point)

def define_type(first_argv_point, second_argv_point):
    '''Define the type of the arguments (integer, float) and the pow less than 0.'''

    type_first_argv = first_argv_point.find(".")
    type_second_argv = second_argv_point.find(".")

    if type_first_argv != -1:
        number = float(first_argv_point)
    else:
        number = int(first_argv_point)

    if type_second_argv != -1:
        pow = float(second_argv_point)
    else:
        pow = int(second_argv_point)

    if pow <= 0 :
       print ("erreur")
       exit()
    calculation_pow(number, pow)

def calculation_pow(number, pow):
    '''This loops do the calcultion and give the result.'''
    i = 1
    while pow != 0:
       result = i*number
       i = result
       pow -= 1
    print (result)
    exit()

lenght_argv()
is_number_check()
calculation_pow()