from tkinter import *

class userinterface(object):
    #def click() :
    #    pass   
    def first_step():
        root = Tk()
        root.title("first step")
        root.resizable(0,0)
        w = 400
        h = 200
        y = 300
        x = 300
        root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        l = Label(root,text = "Please choose",font=("Arial", 14))
        l.place(x=0,y=0)
        b1 = Button(text="add household",width=20,height=10,font=("Arial,4"),command=click())
        b2 = Button(text="add person",width=20,height=10,font=("Arial,4"))
   
        b1.pack(side = LEFT)
        b2.pack(side = LEFT)
        l.pack()
        root.mainloop()
    
    first_step()
   
