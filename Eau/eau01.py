'''Créez un programme qui affiche toutes les différentes combinaisons
de deux nombre entre 00 et 99 dans l’ordre croissant.

Exemples d’utilisation :
$> python exo.py
00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
$>
'''

#Functions
def generate_first_sequence_numbers():
    first_sequence_list = []
    for first_bloc_sequence in range(99):
        for tens_sequence in range(10):
            for unit_sequence in range(10):
                to_string_tens_bloc = str(tens_sequence)
                to_string_unit_bloc = str(unit_sequence)
                sequence_number = to_string_tens_bloc + to_string_unit_bloc
                first_sequence_list.append(sequence_number)
    return first_sequence_list


def generate_second_sequence_numbers(first_sequence):
    second_sequence_list = []
    count = 0
    for number in first_sequence:
        if int(number) == 00:
            count += 1
            unit_sequence = count % 10
            tens_sequence = count // 10
            to_string_unit = str(unit_sequence)
            to_string_tens = str(tens_sequence)
            sequence_number = to_string_tens + to_string_unit
            second_sequence_list.append(sequence_number)
    return second_sequence_list


def creation_last_sequence(first_sequence_bloc, second_sequence_bloc):
    final_sequence = []
    for first_bloc in first_sequence_bloc:
        to_string_first_bloc = str(first_bloc)
        for second_bloc in second_sequence_bloc:
            to_string_second_bloc = str(second_bloc)
            assembly_of_sequences = to_string_second_bloc + " " + to_string_first_bloc
            final_sequence.append(assembly_of_sequences)
    return final_sequence

#resolution
first_sequence_number = generate_first_sequence_numbers()
second_sequence_number = generate_second_sequence_numbers(first_sequence_number)
last_sequence = creation_last_sequence(first_sequence_number, second_sequence_number)

result = ", ".join(last_sequence)

#display
print(result)