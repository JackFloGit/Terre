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


a=[]
for x in range(97,123):
    a.append(chr(x))
alphabet=''.join(a)
print(alphabet)
