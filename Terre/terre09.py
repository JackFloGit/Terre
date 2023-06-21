'''Créez un programme qui affiche la racine carrée 
   d’un entier positif.

 exp : 
       --> script.py 9
           3

!! gerer potentielle erreurs arguments !! '''


import sys


def lenght_argv():
   if len(sys.argv[1:]) != 1:
      print ("erreur")
      exit ()


def check_is_number():
   for argument in sys.argv[1:]:
      t_f = True
      if argument < chr(48) or argument > chr(57):
         t_f = False
   if not t_f:
      print ("erreur")
      exit ()
   integer_check(argument)

def integer_check(argument):
   replace_coma = argument.replace(",",".")
   search_point = replace_coma.find(".")
   if search_point != -1:
      print("erreur")
      exit()
   display_square_root(argument)

def display_square_root(argument):
   '''Genrates and display in the correct form the square root.'''

   argument_is_integer = int(argument)
   calculation_square_root = (argument_is_integer)**(0.5)
   to_str_the_result = str(calculation_square_root)
   end_of_result = to_str_the_result.endswith('.0')

   if end_of_result is True:
      result_is_integer = int(calculation_square_root)
      print(result_is_integer)
      exit()
   else:
      print(calculation_square_root)
      exit()

lenght_argv()
check_is_number()