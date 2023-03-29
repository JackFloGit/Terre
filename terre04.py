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

if len(sys.argv[1:]) < 1:          
 print("Bien essayé mais il faut des chiffres entiers !")   
else :
      if len(sys.argv[1:]) >= 1 :  # arg= 0 ou 1 
      
        arg = ''.join(sys.argv[1:])
        if arg[0] == '-':
          arg = arg[1:]
      t_f = True
      
      for num in arg:
          if num < chr(48) or num > chr(57):
              t_f = False
      if not t_f:
          print("Bien essayer mais il faut des chiffres eniers !")
      else :                                                        # arg integer != float or ascii.letter
           if int(num) % 2 == 0:
                 print("pair") 
           if int(num) % 2 != 0 :
             print ("impair")

