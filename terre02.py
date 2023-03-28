#consigne
#
#Créez un programme qui affiche les arguments
#qu’il reçoit ligne par ligne,
#peu importe le nombre d’arguments.
#
# exp:
#       --> python exo.py je suis solide !
#           je
#           suis
#           solide
#           !
#       -->
#

import sys
for arg in sys.argv[1:]:
    print(arg)
