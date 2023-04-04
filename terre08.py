# Créez un programme qui affiche le résultat d’une puissance.
#L’exposant ne pourra pas être négatif.
#
#   exp:
#      --> python exo.py 2 3
#          8           
#
#   !! gérer les potentielles erreurs d’arguments. !!


import sys

if len(sys.argv[1:]) !=2:
    print ("erreur 1") 
    exit ()
else : 
    for arg0 in sys.argv[1:]:
          if arg0[0] == '-':
                arg0 = arg0[0]
    t_f = True

    if arg0 < chr(48) or arg0 > chr(57) : 
            t_f = False

if not t_f:
    print ("erreur 2")
    exit()
else: 
            num = int(sys.argv[1])
            pow = int (sys.argv[2])
if num == float (sys.argv[1]) and pow != float (sys.argv[2]):
    print("erreur 3")
    exit()
else :
 result = (num)**(pow)
print(result)
