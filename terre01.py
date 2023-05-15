#consigne
#
#Créez un programme qui affiche son nom de fichier.
# exp:
#       --> print exo.py
#           exo.py
#        -->
#       

import sys


def display_first_argument():
    print(sys.argv[0])
    
display_first_argument()