class item(object):


"
function: item verwaltet all existing items
"

"
attributes(5):
-price 
-when was it bought
-who is using item
-status: how much's left (can be none if it doesn't
have any information about amount, also none 
when it's empty)
-sort of item (same items are combined to a new one if
they're shared, but old ones still exist until they're empty(because they carry information about price for each user))

methods():




"

    def __init__(self,price,users,date,status,sort):
        self.price = price
	self.users = users
	self.date = date
	self.status = status
	self.sort = sort

