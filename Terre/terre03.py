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


def lenght_argument():
    if len(sys.argv[1:]) != 1 or len(sys.argv[1]) != 1:
         print("erreur")
         exit()


def letter_check(): 
    alpha = sys.argv[1].isalpha()
    if not alpha:
     print("erreur")
     exit()


def display_rest_alphabet():
    letter = string.ascii_lowercase
    alphabet=''.join(letter)
    for x in alphabet:
         if x == sys.argv[1] :
              y=alphabet.index(x)
    print(alphabet[y:])
            
lenght_argument()
letter_check()
display_rest_alphabet()















#terre01 aff nom prog
#import os

#file = os.path.basename(__file__)
#print(file)

