# Benjamin Kruskamp
# CS162
# Project 3

from tkinter import *

class calc():

    def __init__(self):
        self.root = Tk()
        self.root.title("Simple Calculator")

        self.result = Entry(self.root, width = 35, borderwidth = 5)
        self.result.grid(row=0, column=0, columnspan=6, padx = 10, pady = 10)

        # buttons
        self.b1 = Button(self.root, text="1", width=5, command=lambda: self.button_click('1'))
        self.b1.grid(row=3, column=0, padx=5, pady=5)

        self.b2 = Button(self.root, text="2", width=5, command=lambda: self.button_click('2'))
        self.b2.grid(row=3, column=1, padx=5, pady=5)

        self.b3 = Button(self.root, text="3", width=5, command=lambda: self.button_click('3'))
        self.b3.grid(row=3, column=2, padx=5, pady=5)

        self.b4 = Button(self.root, text="4", width=5, command=lambda: self.button_click('4'))
        self.b4.grid(row=2, column=0, padx=5, pady=5)

        self.b5 = Button(self.root, text="5", width=5, command=lambda: self.button_click('5'))
        self.b5.grid(row=2, column=1, padx=5, pady=5)

        self.b6 = Button(self.root, text="6", width=5, command=lambda: self.button_click('6'))
        self.b6.grid(row=2, column=2, padx=5, pady=5)

        self.b7 = Button(self.root, text="7", width=5, command=lambda: self.button_click('7'))
        self.b7.grid(row=1, column=0, padx=5, pady=5)

        self.b8 = Button(self.root, text="8", width=5, command=lambda: self.button_click('8'))
        self.b8.grid(row=1, column=1, padx=5, pady=5)

        self.b9 = Button(self.root, text="9", width=5, command=lambda: self.button_click('9'))
        self.b9.grid(row=1, column=2, padx=5, pady=5)

        self.b0 = Button(self.root, text="0", width=5, command=lambda: self.button_click('0'))
        self.b0.grid(row=4, column=0, padx=5, pady=5)

        # basic operations
        self.bplus = Button(self.root, text="+", width=5, command=lambda: self.button_click('+'))
        self.bplus.grid(row=1, column=3, padx=5, pady=5)

        self.bminus = Button(self.root, text="-", width=5, command=lambda: self.button_click('-'))
        self.bminus.grid(row=2, column=3, padx=5, pady=5)

        self.bdelete = Button(self.root, text="Del", width=5, command=lambda: self.delete())
        self.bdelete.grid(row=3, column=3, padx=5, pady=5)

        self.bresult = Button(self.root, text="=", width=5, command=lambda: self.calculate())
        self.bresult.grid(row=4, column=3, padx=5, pady=5)

        self.root.mainloop()

    def button_click(self, number):
        current = self.result.get()
        self.result.delete(0, END)
        self.result.insert(0, current + number)

    def delete(self):
        x = self.result.get()
        self.result.delete(0, 'end')
        y = x[:-1]
        self.result.insert(0, y)

    def calculate(self):
        x = self.result.get()
        ans = eval(x)
        self.result.delete(0, 'end')
        self.result.insert(0, ans)

if __name__ == "__main__":
    calc()