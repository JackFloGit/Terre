'''Créez un programme qui affiche toutes les différentes combinaisons
possibles de trois chiffres dans l’ordre croissant,
dans l’ordre croissant. La répétition est volontaire.

Exemples d’utilisation :
$> python exo.py
012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
$>


987 n’est pas là parce que 789 est présent.

020 n’est pas là parce que 0 apparaît deux fois.

021 n’est pas là parce que 012 est présent.

000 n’est pas là parce que cette combinaison ne comporte pas exclusivement
des chiffres différents les uns des autres.
'''



# Functions
def generate_3_figure_number():
    list_combination = []
    for first_sequence in range(10):
        for second_sequence in range(10):
            for third_sequence in range(10):
                  hundreds_place = str(first_sequence)
                  tens_place = str(second_sequence)
                  units = str(third_sequence)
                  expression = hundreds_place + tens_place + units
                  if int(expression[0]) < int(expression[1]) and int(expression[1]) < int(expression[2]):
                      list_combination.append(expression)
    return list_combination

# Resolution
list_unsorted = generate_3_figure_number()

# Display
sequence = ', '.join(list_unsorted)
print(sequence)