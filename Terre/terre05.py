# Créez un programme qui affiche
#  le résultat et le reste d’une division entre deux nombres.
#
# exp :
#       --> python exo.py 5 2
#           resultat : 2
#           reste : 1
#
#       --> python exo.py 10 0
#           erreur.
#
#       --> python exo.py 3 5
#           erreur.

import sys


def lenght_argument():
    if len(sys.argv[1:]) != 2:
        print ("il faut un dividende et un diviseur")
        exit()


def int_numbers_check():
    is_first_arg_digit=(sys.argv[1]).isdigit()
    is_second_arg_digit=(sys.argv[2]).isdigit()
    if not is_first_arg_digit or not is_second_arg_digit:
        print("Bien essayer mais il faut des chiffres entiers !")
        exit()


def calculation_rules():
    dividende = int(sys.argv[1])
    diviseur = int(sys.argv[2])
    if dividende < diviseur:
        print("Erreur le diviseur doit être inférieur au dividende")
        exit()
    if diviseur == 0:
        print ("Erreur le diviseur ne peut pas être nul")
        exit()


def generate_result():
    dividende = int(sys.argv[1])
    diviseur = int(sys.argv[2])
    quotient = (dividende) // (diviseur)
    print ('resultat :',quotient)
    reste = dividende % diviseur
    print ('reste :',reste)

lenght_argument()
int_numbers_check()
calculation_rules()
generate_result()