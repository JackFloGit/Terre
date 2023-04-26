# Créez un programme qui transforme une heure  
# affichée en format 24h en
# une heure affichée en format 12h.
#
# exp : 
#       --> python script.py 23:40
#           11:40PM
#
# !! attention midi et minuit !!
#

import sys

# format
if len(sys.argv[1:]) != 1:
    print("erreur")
    exit()

found=sys.argv[1].find(":")
if found == -1:
    print ("erreur")
    exit()


for arg in sys.argv[1:]:  
 point=arg.find(":")

bloc1=arg[:(point)]
bloc2=arg[((point)+1):]

if len(bloc1) != 2:
   print("erreur")
   exit()


if len(bloc2) != 2:
   print("erreur")
   exit()

#chiffre
isdig1=bloc1.isdigit()
isdig2=bloc2.isdigit()

if isdig1 != True or isdig2 != True:
    print("erreur")
    exit()

# horaire
heure=int(bloc1)
minute=int(bloc2)


if heure < 0 or heure > 23:
    print ("erreur")
    exit()

if minute < 0 or minute > 59:
    print ("erreur")
    exit()



if heure < 1:
   print ((str(heure+12))+(arg[point])+(str(bloc2))+"AM")
   exit()
if heure == 12:
   print((str(heure))+(arg[point])+(str(bloc2))+"PM")
   exit()

if heure < 12:
   print((str(heure))+(arg[point])+(str(bloc2))+"AM")
   exit()
else:
   if heure > 12:
      print ((str(heure-12))+(arg[point])+(str(bloc2))+"PM")
      exit()
