# Créez un programme qui prend en paramètre trois entiers 
# et affiche la valeur du milieu.
#
#   exp :
#           --> python script.py 11 40 34
#               34
#           --> python script.py 2 1 3
#               2
#           --> python script.py 2 2 2
#               erreur.
#

import sys

if len(sys.argv[1:]) != 3:
    print("erreur")
    exit() 
    
isdig0=(sys.argv[1]).isdigit()
isdig1=(sys.argv[2]).isdigit()
isdig2=(sys.argv[3]).isdigit()

if isdig0 is False:
    print("erreur")
    exit()

if isdig1 is False:
    print("erreur")
    exit() 

if isdig2 is False:
    print("erreur")
    exit()
int0=int(sys.argv[1])
int1=int(sys.argv[2])
int2=int(sys.argv[3])

if int0 == int1:
    print("erreur")
    exit()
if int0 == int2:
    print("erreur")
    exit()
if int1 == int2:
    print("erreur")
    exit()

Arg=[]
Arg.append(int0)

if (int1) < (Arg[0]):
    Arg.insert(0,int1)
else:
    Arg.append(int1)
if (int2) < (Arg[0]):
    Arg.insert(0,int2)
elif (int2) < (Arg[1]):
    Arg.insert(1,int2)
else:
    Arg.append(int2)

print(Arg[1])
