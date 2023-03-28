#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en
# argument en lettres minuscules suivi d’un retour à la ligne.
#
#   exp : 
#       --> python exo.py n
#           nopqrstuvwxyz
#       -->
#

import string
import sys


letter = string.ascii_lowercase
alphabet=''.join(letter)
for arg in sys.argv[1:]:
      
 for x in alphabet:
            if x == arg :
               y=alphabet.index(x)
print(alphabet[y:])
            
















#terre01 aff nom prog
#import os

#file = os.path.basename(__file__)
#print(file)

