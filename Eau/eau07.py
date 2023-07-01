'''
#Functions
#Error_Management
#Parsing
#Problem_Solving
#Display

Créez un programme qui met en majuscule la première lettre 
de chaque mot d’une chaîne de caractères. Les autres lettres 
devront être en minuscules. Les mots ne sont délimités que 
par un espace, une tabulation ou un retour à la ligne.

Exemples d’utilisation :
$> python exo.py “bonjour mathilde, comment vas-tu ?!”
Bonjour Mathilde, Comment Vas-tu ?!

$> python exo.py 42
error

Afficher error et quitter le programme en cas de problèmes 
d’arguments.
'''
import sys

#Functions
def upper_first_letter(string):
    string = string[0].upper() + string[0+1:]
    for index in range(len(string)):
        if string[index] == " ":
            string = string[:index + 1] + string[index +1].upper() + string[index + 2:] 
    return string

#Error_Management
if len(sys.argv[1:]) != 1:
    print("error")
    exit()

for character in sys.argv[1]:
    if character > chr(48) and character < chr(57):
        print("error")
        exit()

#Parsing
argument_string = sys.argv[1]

#Problem_Solving
capitalize_words = upper_first_letter(argument_string)

#Display
print(capitalize_words)