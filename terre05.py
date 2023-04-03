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

if len(sys.argv[1:]) != 2 :                                     #1
     print ("il faut un dividende et un diviseur")
     exit()
else:
  for arg in sys.argv[1:]: 
    if arg[0] == '-':
      arg = arg[1:]
  
  t_f = True

if arg < chr(48) or arg > chr(57):
        t_f = False
if not t_f:
    print("Bien essayer mais il faut des chiffres entiers !")   #2
                                                                #1-2 : 2 entité numérique entière

nbr0=sys.argv[1]      #divende            #3
nbr1=sys.argv[2]      #diviseur

num0=int(nbr0)
num1=int(nbr1)

if num0 < num1:
    print("Erreur le diviseur doit être inférieur au dividende")
    exit()
else :   
  if num1 == 0:
    print ("Erreur le diviseur ne peut pas être nul")  
    exit()
  else:



    quotient = (num0) // (num1)
print ('resultat :',quotient)

reste = num0 % num1 
print ('reste :',reste)                       #4. #3-4 : Calcul d'entier dont le diviseur est > 0 et du dividende
