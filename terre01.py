#consigne
#
#Créez un programme qui affiche son nom de fichier.
# exp:
#       --> print exo.py
#           exo.py
#        -->
#       

import os

file = os.path.basename(__file__)
print(file)
