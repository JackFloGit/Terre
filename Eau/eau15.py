'''
Créez un programme qui célèbre votre victoire.


Exemples d’utilisation :
$> ruby exo.rb
J’ai terminé l’Épreuve de l’Eau et c’était [].
$>

Note : [] est à remplacer par un adjectif de votre choix (facile ?)

'''
def sentence_victory():
    sentence = "J’ai terminé l’Épreuve de l’Eau et c’était plus organisé que la terre"
    return sentence
victory = sentence_victory()
print(victory)
