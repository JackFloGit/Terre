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

if len(sys.argv[1:]) != 1:
    print("erreur 1")
    exit()

rep=sys.argv[1].replace(":","")
digit=rep.isdigit()
if digit == False:
    print("erreur 2")
    exit()

heure = []
H = False
for arg in sys.argv[1:]:
    if len(arg) < 4:
       print ("erreur 3")
       exit()
    if len(arg) > 5:
       print ("erreur 4")
       exit()
    if arg[1] != ":":
     H = True
    if not H:
     heure.append(arg[0])
    else:
     if H:
      heure.append(arg[0:2])

for h in heure:
    inth=int(h)
    if inth > 23 :
     print("erreur 3")
     exit()

if inth == 0:
    mid = str(12)
    if not H:
       midn= mid + arg[1:4]+"AM"
    else:
       midn= mid + arg[2:5]+"AM"
    print(midn)
    exit()


if inth == 12:
    midd= arg +"PM"
    print(midd)
    exit()

if inth > 12:
    h_12=(inth)-12
    h12= str(h_12) + arg[2:5]+"PM"
    print(h12)
    exit()
else:
     if not H:
       am= str(inth) + arg[1:5]+"AM"
       print(am)
       exit()
     else:
        am= str(inth) + arg[2:5]+"AM"
        print(am)
        exit()