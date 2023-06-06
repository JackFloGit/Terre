'''Créez un programme qui transforme une heure 
 affichée en format12h en une heure affichée 
 au format 24h.

 exp :
       -->python script.py 11:40PM
          23:40
 !! attention à midi et minuit !!'''


import sys


def argurment_format():
    if len(sys.argv[1:]) != 1:
        print("erreur")
        exit()
    search_ellipsis = sys.argv[1].find(":")
    if search_ellipsis == -1:
        print ("erreur")
        exit()


def check_suffix():
    for argument in sys.argv[1:]:
        ellipsis_index = argument.find(":")
        search_M_ = argument.find("M")
        if search_M_ == -1:
            print("erreur")
            exit()
        bloc_hours = argument[:(ellipsis_index)]
        bloc_minutes = argument[(ellipsis_index)+1:(search_M_)-1]
        am_pm = argument[(search_M_)-1:(search_M_)+1]
        suffix_is_letter = am_pm.isalpha()
        if not suffix_is_letter:
            print("erreur")
            exit()
        if am_pm != "AM" and am_pm != "PM":
            print("erreur")
            exit()
        check_is_figure(bloc_hours, bloc_minutes, am_pm, argument, ellipsis_index)

def check_is_figure(bloc_hours, bloc_minutes, am_pm, argument, ellipsis_index):
    if len(bloc_hours) < 1 or len(bloc_hours) > 2:
        print ("erreur")
        exit()
    if len(bloc_minutes) != 2:
        print ("erreur")
        exit()
    bloc_hours_is_figure = bloc_hours.isdigit()
    bloc_minutes_is_figure = bloc_minutes.isdigit()
    if not bloc_hours or not bloc_minutes:
        print("erreur")
        exit()
    schedule_24H(bloc_hours, bloc_minutes, am_pm, argument, ellipsis_index)


def schedule_24H(bloc_hours, bloc_minutes, am_pm, argument, ellipsis_index):
    hours = int(bloc_hours)
    minutes = int(bloc_minutes)
    if hours < 1 or hours > 12:
        print ("erreur")
        exit()
    if minutes < 0 or minutes > 59:
        print ("erreur")
        exit()
    if am_pm != "PM":
        if hours != 12:
            if hours < 10:
             print ('0' + bloc_hours + argument[ellipsis_index] + bloc_minutes)
             exit()
            else:
                print (bloc_hours + argument[ellipsis_index] + bloc_minutes)
                exit()
        else:
            morning = hours-12
            print('0'+ str(morning) + argument[ellipsis_index] + bloc_minutes)
            exit()
    else:
        if hours != 12:
            afternoon = hours+12
            print(str(afternoon) + argument[ellipsis_index] + bloc_minutes)
            exit()
        else:
            print(str(hours) + argument[ellipsis_index] + bloc_minutes)
            exit()

argurment_format()
check_suffix()