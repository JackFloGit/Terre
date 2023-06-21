#consigne 
#
#Créez un programme qui affiche l’alphabet 
#en lettres minuscules suivi d’un retour à la ligne.
#
#exp:
#       --> python.py
#           abcdefghijklmnopqrstuvwxyz
#       -->
#

def display_alphabet():
   a = []
   for x in range(97,123):
      a.append(chr(x))
   alphabet=''.join(a)
   print(alphabet)

display_alphabet()