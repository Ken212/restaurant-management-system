from tkinter import *
import random
import time

root = Tk()
root.state('zoomed')  # This will open the window in a maximized state
root.title("Restaurant Management System")

# Updated colors for a more inviting appearance
bg_color = "#e6f2ff"
fg_color = "#003366"
button_bg = "#99ccff"
button_fg = "#003366"
entry_bg = "#ffffff"

Tops = Frame(root, bg=bg_color, width=1600, height=500, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, bg=bg_color, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, bg=bg_color, width=450, height=700, relief=SUNKEN, padx=20)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))
lblinfo = Label(Tops, font=("arial", 30, "bold"), text="Restaurant Management System", fg=fg_color, bg=bg_color, bd=10, anchor=W)
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=("arial", 30, "bold"), text=localtime, fg=fg_color, bg=bg_color, anchor=W)
lblinfo.grid(row=1, column=0)

text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg=entry_bg, justify='right')
txtdisplay.grid(columnspan=4, pady=10)

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")

def equals():
    global operator
    try:
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ''
    except:
        text_Input.set("Error")
        operator = ''

def ref():
    x = random.randint(12000, 50000)
    randomRef = str(x)
    rand.set(randomRef)

    fries = float(Fries.get() or 0)
    lunch_meal = float(Large_Fries.get() or 0)
    burger_meal = float(Burger.get() or 0)
    pizza_meal = float(Filet.get() or 0)
    cheese_burger = float(Cheese_Burger.get() or 0)
    drinks = float(Drinks.get() or 0)

    fries_cost = fries * 7.50
    lunch_cost = lunch_meal * 12.50
    burger_cost = burger_meal * 10.50
    pizza_cost = pizza_meal * 15.00
    cheese_burger_cost = cheese_burger * 9.00
    drinks_cost = drinks * 2.50

    meal_cost = fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + drinks_cost

    tax_payable = meal_cost * .0825
    totalcost = meal_cost
    ser_charge = meal_cost * .02
    overallcost = meal_cost + tax_payable + ser_charge

    meal_cost = "$ " + str('%.2f' % meal_cost)
    service = "$ " + str('%.2f' % ser_charge)
    overallcost = "$ " + str('%.2f' % overallcost)
    paidtax = "$ " + str('%.2f' % tax_payable)

    Service_Charge.set(service)
    Cost.set(meal_cost)
    Tax.set(paidtax)
    Sub_Total.set(meal_cost)
    Total.set(overallcost)

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Large_Fries.set("")
    Burger.set("")
    Filet.set("")
    Sub_Total.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Cheese_Burger.set("")

button_config = {
    "padx": 16, "pady": 16, "bd": 4, "fg": button_fg, "font": ('arial', 20, 'bold'), "bg": button_bg
}

btn7 = Button(f2, text='7', command=lambda: btnclick(7), **button_config)
btn7.grid(row=2, column=0)

btn8 = Button(f2, text='8', command=lambda: btnclick(8), **button_config)
btn8.grid(row=2, column=1)

btn9 = Button(f2, text='9', command=lambda: btnclick(9), **button_config)
btn9.grid(row=2, column=2)

Addition = Button(f2, text='+', command=lambda: btnclick('+'), **button_config)
Addition.grid(row=2, column=3)

btn4 = Button(f2, text='4', command=lambda: btnclick(4), **button_config)
btn4.grid(row=3, column=0)

btn5 = Button(f2, text='5', command=lambda: btnclick(5), **button_config)
btn5.grid(row=3, column=1)

btn6 = Button(f2, text='6', command=lambda: btnclick(6), **button_config)
btn6.grid(row=3, column=2)

Subtraction = Button(f2, text='-', command=lambda: btnclick('-'), **button_config)
Subtraction.grid(row=3, column=3)

btn1 = Button(f2, text='1', command=lambda: btnclick(1), **button_config)
btn1.grid(row=4, column=0)

btn2 = Button(f2, text='2', command=lambda: btnclick(2), **button_config)
btn2.grid(row=4, column=1)

btn3 = Button(f2, text='3', command=lambda: btnclick(3), **button_config)
btn3.grid(row=4, column=2)

Multiply = Button(f2, text='*', command=lambda: btnclick('*'), **button_config)
Multiply.grid(row=4, column=3)

btn0 = Button(f2, text='0', command=lambda: btnclick(0), **button_config)
btn0.grid(row=5, column=0)

btnc = Button(f2, text='c', command=clrdisplay, **button_config)
btnc.grid(row=5, column=1)

decimal = Button(f2, text='.', command=lambda: btnclick('.'), **button_config)
decimal.grid(row=5, column=2)

Division = Button(f2, text='/', command=lambda: btnclick('/'), **button_config)
Division.grid(row=5, column=3)

btnequal = Button(f2, text='=', command=equals, **button_config)
btnequal.grid(row=6, columnspan=4, pady=10)

rand = StringVar()
Fries = StringVar()
Large_Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
Sub_Total = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Cheese_Burger = StringVar()

label_config = {
    "font": ('arial', 16, 'bold'), "fg": fg_color, "bg": bg_color, "bd": 10, "anchor": "w"
}
entry_config = {
    "font": ('arial', 17, 'bold'), "bd": 6, "insertwidth": 4, "bg": entry_bg, "justify": 'right'
}

lblreference = Label(f1, text='Order No.', **label_config)
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, textvariable=rand, **entry_config)
txtreference.grid(row=0, column=1)

lblfries = Label(f1, text='Fries Meal', **label_config)
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, textvariable=Fries, **entry_config)
txtfries.grid(row=1, column=1)

lbllargefries = Label(f1, text='Lunch Meal', **label_config)
lbllargefries.grid(row=2, column=0)
txtlargefries = Entry(f1, textvariable=Large_Fries, **entry_config)
txtlargefries.grid(row=2, column=1)

lblburger = Label(f1, text='Burger Meal', **label_config)
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, textvariable=Burger, **entry_config)
txtburger.grid(row=3, column=1)

lblfilet = Label(f1, text='Pizza Meal', **label_config)
lblfilet.grid(row=4, column=0)
txtfilet = Entry(f1, textvariable=Filet, **entry_config)
txtfilet.grid(row=4, column=1)

lblcheeseburger = Label(f1, text='Cheese Burger', **label_config)
lblcheeseburger.grid(row=5, column=0)
txtcheeseburger = Entry(f1, textvariable=Cheese_Burger, **entry_config)
txtcheeseburger.grid(row=5, column=1)

lbldrinks = Label(f1, text='Drinks', **label_config)
lbldrinks.grid(row=0, column=2)
txtdrinks = Entry(f1, textvariable=Drinks, **entry_config)
txtdrinks.grid(row=0, column=3)

lblcost = Label(f1, text='Cost', **label_config)
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, textvariable=Cost, **entry_config)
txtcost.grid(row=1, column=3)

lblservicecharge = Label(f1, text='Service Charge', **label_config)
lblservicecharge.grid(row=2, column=2)
txtservicecharge = Entry(f1, textvariable=Service_Charge, **entry_config)
txtservicecharge.grid(row=2, column=3)

lbltax = Label(f1, text='Tax', **label_config)
lbltax.grid(row=3, column=2)
txttax = Entry(f1, textvariable=Tax, **entry_config)
txttax.grid(row=3, column=3)

lblsubtotal = Label(f1, text='Sub-Total', **label_config)
lblsubtotal.grid(row=4, column=2)
txtsubtotal = Entry(f1, textvariable=Sub_Total, **entry_config)
txtsubtotal.grid(row=4, column=3)

lbltotal = Label(f1, text='Total', **label_config)
lbltotal.grid(row=5, column=2)
txttotal = Entry(f1, textvariable=Total, **entry_config)
txttotal.grid(row=5, column=3)

btnTotal = Button(f1, padx=16, pady=8, bd=10, fg=button_fg, font=('arial', 16, 'bold'), width=10, text='TOTAL', bg=button_bg, command=ref)
btnTotal.grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=10, fg=button_fg, font=('arial', 16, 'bold'), width=10, text='RESET', bg=button_bg, command=reset)
btnReset.grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=10, fg=button_fg, font=('arial', 16, 'bold'), width=10, text='EXIT', bg=button_bg, command=qexit)
btnExit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x300")
    roo.title("Price List")

    # Modernize the price list window
    bg_color_price = "#e6f2ff"
    fg_color_price = "#003366"

    x = Frame(roo, bg=bg_color_price, width=600, height=300, relief=SUNKEN)
    x.pack(side=TOP)
    lblinfo = Label(x, font=('arial', 15, 'bold'), text='ITEM', fg=fg_color_price, bg=bg_color_price, bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(x, font=('arial', 15, 'bold'), text='----------', fg=fg_color_price, bg=bg_color_price, anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(x, font=('arial', 15, 'bold'), text='PRICE', fg=fg_color_price, bg=bg_color_price, bd=5, anchor=W)
    lblinfo.grid(row=0, column=5)

    price_list = [
        ("Fries Meal", "7.50"),
        ("Lunch Meal", "12.50"),
        ("Burger Meal", "10.50"),
        ("Pizza Meal", "15.00"),
        ("Cheese Burger", "9.00"),
        ("Drinks", "2.50")
    ]

    for idx, (item, price) in enumerate(price_list, start=1):
        lblinfo = Label(x, font=('arial', 15, 'bold'), text=item, fg=fg_color_price, bg=bg_color_price, anchor=W)
        lblinfo.grid(row=idx, column=0)
        lblinfo = Label(x, font=('arial', 15, 'bold'), text=price, fg=fg_color_price, bg=bg_color_price, anchor=W)
        lblinfo.grid(row=idx, column=5)

    roo.mainloop()

btnPrice = Button(f1, padx=16, pady=8, bd=10, fg=button_fg, font=('arial', 16, 'bold'), width=10, text='PRICE', bg=button_bg, command=price)
btnPrice.grid(row=7, column=0)

root.mainloop()
