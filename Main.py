from tkinter import messagebox
from tkinter import *
# from tkinter.tix import COLUMN
# from turtle import up

root = Tk()


root.geometry("600x600")
root.title("Inventory")


# my variables

ground = IntVar(root, 16)
Creamer = IntVar(root, 16)
Sugar = IntVar(root, 16)
Cups = IntVar(root, 10)

items = IntVar(root, 0)

c_sugar = StringVar(root, 0)
c_ground = StringVar(root, 0)
c_creamer = StringVar(root, 0)
c_cups = StringVar(root, 0)


Sales = IntVar(root, 0)
Expenses = IntVar(root, 0)
Profit = IntVar(root, 0)


selected = StringVar(root, "")


# my Functions

def change_selected():
    selected.set(selected.get()+"cream")


def change_selected2():
    selected.set(selected.get() + "sugar")


def change_ground():
    print(c_ground.get())
    c_ground.set(16)
    print(c_ground.get())


def change_creamer():
    print(c_creamer.get())
    c_creamer.set(16)
    print(c_creamer.get())


def change_cups():
    print(c_cups.get())
    c_cups.set(10)
    print(c_cups.get())


def change_sugar():
    print(c_sugar.get())
    c_sugar.set(16)
    print(c_sugar.get())

# A Functions to update the inventory


# This is a function that is used to update the inventory
def updates():
    ground.set(int(ground.get())+int(c_ground.get()))

    Creamer.set(int(Creamer.get())+int(c_creamer.get()))

    Cups.set(int(Cups.get())+int(c_cups.get()))

    Sugar.set(int(Sugar.get())+int(c_sugar.get()))
    print(int(Expenses.get()))
    Expenses.set(int(Expenses.get()) + (int(c_sugar.get())*1) +
                 (int(c_creamer.get())*2) + (int(c_cups.get())*4) + (int(c_ground.get())*20))

# This is a function that is used to complete the order


def orders():
    print(ent.get())
    print(selected.get())
    if selected.get() == "":

        if (int(Cups.get())-int(ent.get())) > 0:

            Cups.set(int(Cups.get())-int(ent.get()))

            messagebox.showinfo("Success", "Order Successfully Placed")
            Sales.set(int(Sales.get()+(1.50*int(ent.get()))))
            Profit.set(int(Sales.get())-int(Expenses.get()))
        else:

            messagebox.showwarning(
                "Insufficient Inventory", "Not Enough Items")

    elif selected.get() == "cream":
        stock = (int(Creamer.get())-int(ent.get()))
        if stock < 0:

            messagebox.showwarning(
                "Insufficient Inventory", "Not Enough Items")

        else:

            messagebox.showinfo("Success", "Order Successfully Placed")
            if (int(Cups.get())-int(ent.get())) > 0:
                Creamer.set(int(Creamer.get())-1*(int(ent.get())))
                Cups.set(int(Cups.get())-int(ent.get()))
                Sales.set(int(Sales.get()+(1.50*int(ent.get()))))
                Profit.set(int(Sales.get())-int(Expenses.get()))
            else:

                messagebox.showwarning(
                    "Insufficient Inventory", "Not Enough Cups")
    elif selected.get() == "sugar":
        stock = (int(Sugar.get())-int(ent.get()))
        if stock < 0:

            messagebox.showwarning(
                "Insufficient Inventory", "Not Enough Items")

        else:

            if (int(Cups.get())-int(ent.get())) > 0:
                Sugar.set(int(Creamer.get())-1*(int(ent.get())))
                Cups.set(int(Cups.get())-int(ent.get()))
                Sales.set(int(Sales.get()+(1.50*int(ent.get()))))
                Profit.set(int(Sales.get())-int(Expenses.get()))
            else:
                print("there are no sufficient cups in the inventory")
                messagebox.showwarning(
                    "Insufficient Inventory", "Not Enough Items")
    else:
        if (int(Sugar.get())-1) < 0 and (int(Creamer.get())-1) < 0:
            print("Insufficient Inventory")
            messagebox.showwarning(
                "Insufficient Inventory", "Not Enough Sugar")
        else:

            if (int(Cups.get())-int(ent.get())) > 0:
                Sugar.set(int(Sugar.get())-1*(int(ent.get())))
                Creamer.set(int(Creamer.get())-1*(int(ent.get())))

                Cups.set(int(Cups.get())-int(ent.get())-1*(int(ent.get())))
                Sales.set(int(Sales.get()+(1.50*int(ent.get()))))
                Profit.set(int(Sales.get())-int(Expenses.get()))
                messagebox.showinfo("Success", "Order Successfully Placed")
            else:
                print("there are no sufficient cups in the inventory")
                messagebox.showwarning(
                    "Insufficient Inventory", "Not Enough Cups")


# The lables
label1 = Label(root, text="INVENTORY")
label1.grid(row=0, column=0)
label2 = Label(root, text="ADD TO INVENTORY")
label2.grid(row=0, column=2)
label3 = Label(root, text="ORDER FORM")
label3.grid(row=0, column=4)
label4 = Label(root, text="FINAMCIAL DATA")
label4.grid(row=0, column=7, columnspan=2)


label5 = Label(root, text="Grounds")
label5.grid(row=1, column=0)
label6 = Label(root, text="Creamers")
label6.grid(row=2, column=0)
label7 = Label(root, text="Sugar")
label7.grid(row=3, column=0)
label8 = Label(root, text="Cups")
label8.grid(row=4, column=0)


label9 = Label(root, textvariable=ground)
label9.grid(row=1, column=1)
label10 = Label(root, textvariable=Creamer)
label10.grid(row=2, column=1)
label11 = Label(root, textvariable=Sugar)
label11.grid(row=3, column=1)
label12 = Label(root, textvariable=Cups)
label12.grid(row=4, column=1)


cb1 = Checkbutton(root, text="add 16 oz of Grounds ", command=change_ground)
cb1.grid(row=1, column=2)

cb2 = Checkbutton(root, text="add 16 oz of Creamer ", command=change_creamer)
cb2.grid(row=2, column=2)

cb3 = Checkbutton(root, text="add 16 Sugar ", command=change_sugar)
cb3.grid(row=3, column=2)

cb4 = Checkbutton(root, text="add 10 cups ", command=change_cups)
cb4.grid(row=4, column=2)


bt = Button(root, relief='raised', bd=3,
            text="Add to Inventory", command=updates)
bt.grid(row=5, column=2)


label20 = Label(root, text="Quantity")
label20.grid(row=1, column=4)

cb = Checkbutton(root, text="Creamer ", command=change_selected)
cb.grid(row=2, column=4)
cb = Checkbutton(root, text="Sugar ", command=change_selected2)
cb.grid(row=3, column=4)

bt = Button(root, relief='raised', bd=3, text="Place Order", command=orders)
bt.grid(row=4, column=4)
ent = Entry(root, width=3)
ent.grid(row=1, column=6)


# under Finally Data


lf = Label(root, text="Sales").grid(row=1, column=7)

lf = Label(root, text="Expenses").grid(row=2, column=7)

lf = Label(root, text="Profit").grid(row=3, column=7)

# their Values


lf = Label(root, textvariable=Sales).grid(row=1, column=8)

lf = Label(root, textvariable=Expenses).grid(row=2, column=8)

lf = Label(root, textvariable=Profit).grid(row=3, column=8)


root.mainloop()
