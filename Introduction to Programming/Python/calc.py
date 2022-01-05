# Calculator
# # Info on Tkinter
# https://realpython.com/python-gui-tkinter/

# Import only Tk (interface), Widgets - Entry (text input) and Button
from tkinter import Tk, Entry, Button	

gui = Tk()
gui.configure(background="light green")
gui.title("Calculator")
gui.geometry(f"270x300+{gui.winfo_screenwidth()-270}+0")

# Interface Variables
font = "Calibri 16"
c = 3 # number of columns
r = 7 # number of rows
bbg = "white"
bfg = "black"

# Build Graphical User Interface

# Text Input
screen = Entry(gui, fg="red", bg="black", bd=5, font=font)
screen.place(relw=c/c, relh=1/r, relx=0, rely=0)

def btn_click(num):
    screen_contents = screen.get()
    print(num)
    screen.insert(len(screen_contents), str(num))
    
def clear():
    print('Clear')
    screen_contents = screen.get()
    screen.delete(0, len(screen_contents))
    
def calculate():
    screen_contents = screen.get()
    result = str(eval(screen_contents))
    clear()
    screen.insert(len(screen_contents), result)

# Buttons

# Numbers
Button(gui, text="1", fg=bfg, bg=bbg, font=font, command=lambda num=1 : btn_click(num)).place(relw=1/c, relh=1/r, relx=0, rely=1/r)
Button(gui, text="2", fg=bfg, bg=bbg, font=font, command=lambda num=2 : btn_click(num)).place(relw=1/c, relh=1/r, relx=1/c, rely=1/r)
Button(gui, text="3", fg=bfg, bg=bbg, font=font, command=lambda num=3 : btn_click(num)).place(relw=1/c, relh=1/r, relx=2/c, rely=1/r)
Button(gui, text="4", fg=bfg, bg=bbg, font=font, command=lambda num=4 : btn_click(num)).place(relw=1/c, relh=1/r, relx=0, rely=2/r)
Button(gui, text="5", fg=bfg, bg=bbg, font=font, command=lambda num=5 : btn_click(num)).place(relw=1/c, relh=1/r, relx=1/c, rely=2/r)
Button(gui, text="6", fg=bfg, bg=bbg, font=font, command=lambda num=6 : btn_click(num)).place(relw=1/c, relh=1/r, relx=2/c, rely=2/r)
Button(gui, text="7", fg=bfg, bg=bbg, font=font, command=lambda num=7 : btn_click(num)).place(relw=1/c, relh=1/r, relx=0, rely=3/r)
Button(gui, text="8", fg=bfg, bg=bbg, font=font, command=lambda num=8 : btn_click(num)).place(relw=1/c, relh=1/r, relx=1/c, rely=3/r)
Button(gui, text="9", fg=bfg, bg=bbg, font=font, command=lambda num=9 : btn_click(num)).place(relw=1/c, relh=1/r, relx=2/c, rely=3/r)

Button(gui, text="+", fg=bfg, bg=bbg, font=font, command=lambda num="+" : btn_click(num)).place(relw=1/c, relh=1/r, relx=0, rely=4/r)
Button(gui, text="0", fg=bfg, bg=bbg, font=font, command=lambda num=0 : btn_click(num)).place(relw=1/c, relh=1/r, relx=1/c, rely=4/r)
Button(gui, text="-", fg=bfg, bg=bbg, font=font, command=lambda num="-" : btn_click(num)).place(relw=1/c, relh=1/r, relx=2/c, rely=4/r)

Button(gui, text="*", fg=bfg, bg=bbg, font=font, command=lambda num="*" : btn_click(num)).place(relw=1/c, relh=1/r, relx=0, rely=5/r)
Button(gui, text=".", fg=bfg, bg=bbg, font=font, command=lambda num="." : btn_click(num)).place(relw=1/c, relh=1/r, relx=1/c, rely=5/r)
Button(gui, text="/", fg=bfg, bg=bbg, font=font, command=lambda num="/" : btn_click(num)).place(relw=1/c, relh=1/r, relx=2/c, rely=5/r)

Button(gui, text="C", fg="white", bg="red", font=font, command=clear).place(relw=1/c, relh=1/r, relx=0, rely=6/r)
Button(gui, text="=", fg="white", bg="blue", font=font, command=calculate).place(relw=2/c, relh=1/r, relx=1/c, rely=6/r)

# for i in range(1, 4):
#     Button(gui, text="1", fg="black", bg="white", font=font).place(relw=1/c, relh=1/r, relx=i-1/c, rely=1/r)


# Interface functions


# Set everything up
gui.mainloop()

asd = "asd"

asd.capitalize()
