# Créez un programme qui affiche l’inverse de  
# la chaîne de caractères donnée en argument.
#
# exp :
#       --> python exo script.py "Hello world!"
#           !dlrow olleH
#
#       --> python exo script.py "lehciM"
#           Michel
#
#       !! gérer les potentielles erreurs d’arguments.!!
#



import sys

if len(sys.argv[1:]) < 1:          
 print("Bien essayé mais il faut des caractère")
 exit()
else :

 str =' '.join(sys.argv[1:])
reverse =''.join(str[::-1])
print (reverse)


#voir si je peux faire conciderer les cactere spéciaux/  demander cette consigne des arg sur discord