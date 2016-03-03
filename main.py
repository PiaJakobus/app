
#function:beinhaltet die ausfuehrung der anderen dateien

#functions:
#-user_input verarbeiten



def configuration_app():
    input_household = raw_input("Haushalt hinzufuegen->YES/NO")
    if str(input_household) == str("YES"): 
        input_household = raw_input("Name des Haushalts")
        input_household_check = raw_input("Name bestaetigen")
        if str(input_household) == str(input_household_check):
            #household.name_household = input_household
            return("test")
        else:
	    raw_input("Bitte von vorne eingeben, Fehler in der Eingabe")
            configuration_app()
    elif str(input_household) == "NO": 
        return raw_input("Ok,nun zu den Teilnehmern")
    else: 
        raw_input("Fehlerhafte Eingabe (ENTER)")
        configuration_app()


print configuration_app()

#        name_person = input("Bitte Username eingeben")
#        name_person_check = input("Bitte Username bestaetigen")
#        if str(name_person) = str(name_person_check):
#	    household.name_person = name_person
#	else:
#	    input("Namen stimmen nicht ueberein, bitte erneut eingeben")
#	    
#     elif input("Haushalt hinzufuegen->YES/NO") = str('NO'):
#        break
#     else:
#        input("Eingabe nicht korrekt, bitte mit YES or NO antworten")
        



   


#userstring = input("Hauhalt")
#def user_input():
#   if userstring = 
