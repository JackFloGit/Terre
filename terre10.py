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
    print("erreur")
    exit()


arg = sys.argv[1]
num = arg.isdigit()
if num == False:
    print ("erreur")
    exit()
else:
    x = int(arg)

sqrx = (x)**(0.5)
intsqrx = int(sqrx)                                 # racine carré de x

if intsqrx < 2:
    print("Oui,",arg,"est un nombre premier.")
    exit()

unknow = range(2, ((intsqrx)+1))

results = []

for y in unknow:
    rest= (x)%(y)
    results.append(rest)

premier = True

for r in results:
    if r == 0:
        premier = False
        print("Non,",arg,"n'est pas un nombre premier.")
        break
if premier:
    print("Oui,",arg,"est un nombre premier.")

