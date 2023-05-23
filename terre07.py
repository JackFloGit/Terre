# Créez un programme qui affiche le nombre de caractères 
#   d’une chaîne de caractères passée en argument.
#
#   exp:
#       --> python exo.py “Hello world!”
#           12
#
#       --> python exo.py
#           erreur
#
#       --> python exo.py “Bonjour” “Aurevoir”
#           erreur
#
#       --> python exo.py 10
#           erreur

import sys


def lenght_sys_arg():
    if len(sys.argv[1:]) != 1 :
        print("erreur")
        exit()


def argument_is_alpha():
    t_f= False
    for arg in sys.argv[1:]:
        if arg < chr(48) or arg > chr(57):
            t_f = True
    arg_is_digit=arg.isdigit()
    if arg_is_digit or not t_f:
        print("erreur") 
        exit ()

def generate_lenght():
    for string in sys.argv[1:]:
        lenght= 0
        char= string[0]
        while char:
            lenght += 1
            char = string[lenght:lenght+1]
        print(lenght)
        exit()

lenght_sys_arg()
argument_is_alpha()
generate_lenght()