# Créez un programme qui affiche la racine carrée 
# d’un entier positif.
#
# exp : 
#       --> script.py 9
#           3
#
# !! gerer potentielle erreurs arguments !!
#


import sys

if len(sys.argv[1:]) != 1:
  print ("erreur 0")
  exit ()

for arg in sys.argv[1:]:
 t_f = True
 if arg < chr(48) or arg > chr(57):
        t_f = False
 if not t_f:
   print ("erreur 1")
   exit ()
 
 
 replace = arg.replace(",",".")
 float =replace.find(".")
 
 if float != -1:
    print("erreur 2")
    exit()
 else:   
    intarg = int(arg)

racine = (intarg)**(0.5)


str = str(racine)
end = str.endswith('.0')

if end is True:
   int = int(racine)
   print(int)
else:
   print(racine)