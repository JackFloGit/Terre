#Créez un programme qui permet de déterminer 
#si l’argument donné est un entier pair ou impair..
#  !! Attention : gérez aussi les entiers négatifs. !!
#
#   exp
#       --> python exo.py 2
#           pair
#
#       --> python exo.py 5
#           impair
#
#       --> python exo.py Bonjour
#           bien essayer mais il faut des chiffres
#
#       --> python exo.py 
#           bien essayer mais il faut des chiffres
#
#


import sys

if len(sys.argv[1:]) != 1:
    print("Bien essayé mais il faut un seul argument !")
    exit()

arg = ''.join(sys.argv[1:])

if arg[0] == '-':
  arg = arg[1:]

num=arg.isdigit()

if num is False:
    print("Bien essayer mais il faut des chiffres entiers !")
    exit()

if int(arg) %2 != 0 :
  print ("impair")
  exit()
else:
  print("pair")
  exit()