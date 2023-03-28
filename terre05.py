# Créez un programme qui affiche
#  le résultat et le reste d’une division entre deux nombres.
#
# exp :
#       --> python exo.py 5 2
#           resultat : 2
#           reste : 1
#
#       --> python exo.py 10 0
#           erreur.
#
#       --> python exo.py 3 5
#           erreur.


import sys

if len(sys.argv[1:]) < 1:          
 print("Bien essayé mais il faut des chiffres entiers !")   
else :
      if len(sys.argv[1:]) >= 1 :  # arg= 0 ou 1 
      
        arg = ''.join(sys.argv[1:])
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