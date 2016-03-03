class person(object):

"
Function: contains all persons wich have an account and can be associated to at least one household.
"


"attributes(5):
-name  household
-containing persons
-financial situation of single user
-current shared items of single user
-aufgebrauchte items of single user
"

"
Methoden():
-
"

    def __init__(self,name_household,name_persons,financial_situation_user, items_user,personal_consumption):
        self.name_household = name_household
        self.name_persons = []
        self.financial_situation = financial_situation
        self.items_user = items_user
        self.used_items_user = personal_consumption



