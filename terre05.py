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

if len(sys.argv[1:]) != 2 :                                     
     print ("il faut un dividende et un diviseur")
     exit()

for arg in sys.argv[1:]: 
  if arg[0] == '-':
    arg = arg[1:]

isdig0=(sys.argv[1]).isdigit()
isdig1=(sys.argv[2]).isdigit()

if isdig0 is False or isdig1 is False:
    print("Bien essayer mais il faut des chiffres entiers !")
    exit() 
                                         

num0=int(sys.argv[1])   #divende
num1=int(sys.argv[2])   #diviseur 

if num0 < num1:
    print("Erreur le diviseur doit être inférieur au dividende")
    exit() 
if num1 == 0:
    print ("Erreur le diviseur ne peut pas être nul")  
    exit()

quotient = (num0) // (num1)
print ('resultat :',quotient)

reste = num0 % num1 
print ('reste :',reste)
