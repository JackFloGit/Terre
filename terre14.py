# Créez un programme qui détermine si une liste d’entiers est triée ou pas.
#
#
# Exp :
#       --> python script.py 9 8 3
#           Pas triée !
#
#       --> python script.py 3 8 9 12
#           Triée !
#
#       --> python script.py “Salut”
#           erreur.
#

import sys

if len(sys.argv[1:]) < 2:
    print("erreur")
    exit()

liste= []

for arg in sys.argv[1:]:
    if not arg.isdigit():
        print("erreur")
        exit()
    intarg=int(arg)
    liste.append(intarg)

x=len(liste)
i=0
while i < (x-1):
    if liste[i] < liste[((i)+1)]:
        sort=True
    else:
       sort=False

    i=i+1

if sort == True:
    print("Triée !")
else:
    print("Pas triée !")
