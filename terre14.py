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

list0= []
list1= []

for arg in sys.argv[1:]:
    if not arg.isdigit():
        print("erreur")
        exit()
    intarg=int(arg)
    list0.append(intarg)
    list1.append(intarg)

list2=[]

while len(list1) != 0:
    i=list1.index(min(list1))
    list2.append(list1[i])
    list1.pop(i)

if list0 != list2:
    print("Pas triée !")
    exit()
else:
    print("Triée !")
    exit()

