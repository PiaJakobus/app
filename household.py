class household(object):

"
function: household verwaltet die personen die ihm zugeordnet sind 
"

"
attributes(3):
-number of containing persons
-place
-all shared items 
-amount of shared items
-financial situation between each user

methods():
-



"

    def __init__(self,containing_persons,place,shared_items,amonut_shared_items,overview_finances):
        self.containing_persons = containing_persons
	self.place = place
	self.shared_items = shared_items
	self.amount_shared_items = amount_shared_items
	self.overview_finances = overview_finances
