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

if len(sys.argv[1:]) != 1 :
    print("erreur")
    exit()

t_f= False
for arg in sys.argv[1:]:
    if arg < chr(48) or arg > chr(57):
        t_f = True
isdig=arg.isdigit()
if not t_f or isdig is True:
    print("erreur") 
    exit ()
else:
    print (len(arg))
