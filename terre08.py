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
    print ("erreur") 
    exit ()

txt0 = sys.argv[1]                                              #
rep0 = txt0.replace("-","").replace(".","").replace(",","")

txt1 = sys.argv[2]
rep1 = txt1.replace("-","").replace(".","").replace(",","")

num0 = rep0.isdigit()
num1 = rep1.isdigit()

if num0 == False :
    print ("erreur")
    exit()

if num1 == False:  
    print ("erreur")                                        #1   1: verif si arg = num
    exit()



freplace0 = txt0.replace(",",".")                                   #
point0 = freplace0.count(".")
freplace1 = txt1.replace(",",".")
point1 = freplace1.count(".")                                       #2  2: remplacer "," par "."

if point0 > 1:                                                      #
   print ("erreur")
   exit()
if point1 > 1:
   print ("erreur")
   exit()                                                             #3 3: stop si + de 1 "."


test0 = freplace0.find(".")                                         #
test1 = freplace1.find(".")

if test0 != -1: 
   number0 = float(freplace0)
else:
    number0 = int(freplace0)

if test1 != -1:
   number1 = float(freplace1)
else:
    number1 = int(freplace1)                                        #4 4: entier ou decimal 

if number1 < 0 :
   print ("erreur")                                               # exposant positif
   exit()
else:
    pow = (number0)**(number1)
    print (pow)
    exit()


