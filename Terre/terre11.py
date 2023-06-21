'''Créez un programme qui transforme une heure  
 affichée en format 24h en
 une heure affichée en format 12h.

 exp : 
      --> python script.py 23:40
         11:40PM

 !! attention midi et minuit !!'''


import sys


def argument_format():
   '''Check if argument is in the correct format.'''
   if len(sys.argv[1:]) != 1:
      print("erreur")
      exit()

   search_ellipsis = sys.argv[1].find(":")
   if search_ellipsis == -1:
      print ("erreur")
      exit()

   for argument in sys.argv[1:]:
      ellipsis_index = argument.find(":")

   bloc_hours = argument[:(ellipsis_index)]
   bloc_minutes = argument[((ellipsis_index)+1):]

   if len(bloc_hours) != 2 and len(bloc_minutes) != 2:
      print("erreur")
      exit()
   check_is_figure(bloc_hours, bloc_minutes,argument, ellipsis_index)


def check_is_figure(bloc_hours, bloc_minutes,argument, ellipsis_index):
   bloc_hours_is_figure=bloc_hours.isdigit()
   bloc_minutes_is_figure=bloc_minutes.isdigit()

   if not bloc_hours_is_figure or not bloc_minutes_is_figure:
      print("erreur")
      exit()
   schedule(bloc_hours, bloc_minutes,argument, ellipsis_index)


def schedule(bloc_hours, bloc_minutes, argument, ellipsis_index):
   hours = int(bloc_hours)
   minutes = int(bloc_minutes)
   if hours < 0 or hours > 23:
      print ("erreur")
      exit()
   if minutes < 0 or minutes > 59:
      print ("erreur")
      exit()
   if hours < 1:
      print ((str(hours+12))+(argument[ellipsis_index])+(str(bloc_minutes))+"AM")
      exit()
   if hours == 12:
      print((str(hours))+(argument[ellipsis_index])+(str(bloc_minutes))+"PM")
      exit()
   if hours < 12:
      print((str(hours))+(argument[ellipsis_index])+(str(bloc_minutes))+"AM")
      exit()
   else:
      if hours > 12:
         print ((str(hours-12))+(argument[ellipsis_index])+(str(bloc_minutes))+"PM")
         exit()

argument_format()
