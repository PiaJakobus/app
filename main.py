from household import household 
#function:beinhaltet die ausfuehrung der anderen dateien

#functions:
#-user_input verarbeiten


list_of_all_households = []
def configuration_household():
    input_household = input("household add: yes/no")
    if str(input_household) == str("yes"):
        input_household = input("name household")
        input_household_check = input("wiederholen")
        if str(input_household) != str(input_household_check):
            correctur1 = input("please try again")
            correctur2 = input("confirm")
            while str(correctur1) != str(correctur2):
                correctur1 = input("please try again")
                correctur2 = input("confirm")
        list_of_all_households.append(str(input_household))
        configuration_persons(input_household)
        configuration_household()
    elif str(input_household) == str("no"):
        print(household.household_persons)
    else:
        input("fehlerhafte eingabe")
        configuration_household()
		

def configuration_persons(input_household):
    input_persons = input("name of persons of this household getrennt via comma")
    input_persons_check = input("confirm persons")
    if str(input_persons) != str(input_persons_check):
        correctur1 = input("try again")
        correctur2 = input("confirm")
        while str(correctur1)!= str(correctur2):
            correctur1 = input("try again")
            correctur2 = input("confirm")
    household.household_persons[str(input_household)] = str(input_persons).split(",")
    	

configuration_household()
