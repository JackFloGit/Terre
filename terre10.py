# Créez un programme qui affiche si un nombre est 
# premier ou pas.
# 
# exp :
#       --> script.py 5
#           Oui, 5 est un nombre premier.
#
#       --> script.py 6  
#           Non, 6 n'est pas un nombre premier.
#
#   !! 0 et 1 ne sont pas des nombres premiers (gerer erreur)!! 
#

import sys 
import random

if len(sys.argv[1:]) !=1:
    print("erreur 1")
    exit()

t_f=True
                                                #
for arg in sys.argv[1:]:
 if arg < chr(48) or arg > chr(57):
    t_f = False
if not t_f:
   print ("erreur 2")
   exit()

point = arg.replace(",",".")
float = point.find(".")

if float != -1:
   print ("erreur 3")
   exit ()
else :
   x = int(arg)
sqrx = (x)**(0.5)
intsqrx = int(sqrx)
print(intsqrx)


unknow = range(2, ((intsqrx)+1))

results = []

for y in unknow:
  result = (x)/(y)

  results.append(result)

for r in results:
    print(r)

chn = str(r)
end = chn.endswith('.0')
if end is True:
   intg = int(r)
   print("il n'est pas premier")
else:
   print("il est premier")