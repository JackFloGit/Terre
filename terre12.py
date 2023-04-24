# Créez un programme qui transforme une heure 
# affichée en format12h en une heure affichée 
# au format 24h.
#
# exp :
#       -->python script.py 11:40PM
#          23:40
# !! attention à midi et minuit !!
#

import sys

#format/":"
if len(sys.argv[1:]) != 1 :
    print("erreur")
    exit()
found=sys.argv[1].find(":")
if found == -1:
    print ("erreur")
    exit()


    
for arg in sys.argv[1:]:


#lettre

 point=arg.find(":")
ltr=arg.find("M")

if ltr == -1:
    print("erreur")
    exit()

bloc1=arg[:(point)]
bloc2=arg[(point)+1:(ltr)-1]
ampm=arg[(ltr)-1:(ltr)+1]

alpha= ampm.isalpha()

if alpha is False:
    print("erreur")
    exit()

if ampm != "AM" and ampm != "PM":
    print("erreur")
    exit()

#chiffre

if len(bloc1) < 1 or len(bloc1) > 2:
    print ("erreur")
    exit()

if len(bloc2) !=2:
    print ("erreur")
    exit()

isdig1=bloc1.isdigit()
isdig2=bloc2.isdigit()

if isdig1 != True or isdig2 != True:
    print("erreur")
    exit()


#syst24h
point=arg.find(":")
ltr=arg.find("M")

bloc1=arg[:(point)]
bloc2=arg[(point)+1:(ltr)-1]
amapm=arg[(ltr)-1:(ltr)+1]

heure=int(bloc1)
minute=int(bloc2)


if heure < 1 or heure > 12:
    print ("erreur")
    exit()


if minute < 0 or minute > 59:
    print ("erreur")
    exit()


if ampm != "PM":
    if heure != 12:
        if heure < 10:
         print ('0'+bloc1+':'+bloc2)
        else:
            print (bloc1+':'+bloc2)
    else:
        matin=heure-12
        print('0'+str(matin)+':'+bloc2)
else:
    if heure != 12:
        Après_midi=heure+12
        print(str(Après_midi)+':'+bloc2)
    else:
        print(str(heure)+':'+bloc2)
