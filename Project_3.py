# Benjamin Kruskamp
# CS162
# Project 3

from tkinter import *


class calc():

    def __init__(self):
        self.root = Tk()
        self.root.title("Simple Calculator")
        self.root.geometry("360x260")

        self.resultwindow = Entry(self.root)
        self.resultwindow.grid(row=0, column=0, columnspan=6)
        self.resultwindow.config(font=("Roboto", 18))

        # buttons
        self.button1 = Button(self.root, text="1", width=5, command=lambda: self.ins('1'))
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button1.config(font=("Roboto", 18))

        self.button2 = Button(self.root, text="2", width=5, command=lambda: self.ins('2'))
        self.button2.grid(row=1, column=1, padx=5, pady=5)
        self.button2.config(font=("Roboto", 18))

        self.button3 = Button(self.root, text="3", width=5, command=lambda: self.ins('3'))
        self.button3.grid(row=1, column=2, padx=5, pady=5)
        self.button3.config(font=("Roboto", 18))

        self.button4 = Button(self.root, text="4", width=5, command=lambda: self.ins('4'))
        self.button4.grid(row=2, column=0, padx=5, pady=5)
        self.button4.config(font=("Roboto", 18))

        self.button5 = Button(self.root, text="5", width=5, command=lambda: self.ins('5'))
        self.button5.grid(row=2, column=1, padx=5, pady=5)
        self.button5.config(font=("Roboto", 18))

        self.button6 = Button(self.root, text="6", width=5, command=lambda: self.ins('6'))
        self.button6.grid(row=2, column=2, padx=5, pady=5)
        self.button6.config(font=("Roboto", 18))

        self.button7 = Button(self.root, text="7", width=5, command=lambda: self.ins('7'))
        self.button7.grid(row=3, column=0, padx=5, pady=5)
        self.button7.config(font=("Roboto", 18))

        self.button8 = Button(self.root, text="8", width=5, command=lambda: self.ins('8'))
        self.button8.grid(row=3, column=1, padx=5, pady=5)
        self.button8.config(font=("Roboto", 18))

        self.button9 = Button(self.root, text="9", width=5, command=lambda: self.ins('9'))
        self.button9.grid(row=3, column=2, padx=5, pady=5)
        self.button9.config(font=("Roboto", 18))

        self.button0 = Button(self.root, text="0", width=5, command=lambda: self.ins('0'))
        self.button0.grid(row=4, column=0, padx=5, pady=5)
        self.button0.config(font=("Roboto", 18))

        # basic operations
        self.buttonplus = Button(self.root, text="+", width=5, command=lambda: self.ins('+'))
        self.buttonplus.grid(row=1, column=3, padx=5, pady=5)
        self.buttonplus.config(font=("Roboto", 18))

        self.buttonminus = Button(self.root, text="-", width=5, command=lambda: self.ins('-'))
        self.buttonminus.grid(row=2, column=3, padx=5, pady=5)
        self.buttonminus.config(font=("Roboto", 18))

        self.buttondelete = Button(self.root, text="Del", width=5, command=lambda: self.delete())
        self.buttondelete.grid(row=3, column=3, padx=5, pady=5)
        self.buttondelete.config(font=("Roboto", 18))

        self.buttonresult = Button(self.root, text="=", width=5, command=lambda: self.calculate())
        self.buttonresult.grid(row=4, column=3, padx=5, pady=5)
        self.buttonresult.config(font=("Roboto", 18))

        self.root.mainloop()

    def ins(self, val):
        self.resultwindow.insert(END, val)

    def delete(self):
        x = self.resultwindow.get()
        self.resultwindow.delete(0, 'end')
        y = x[:-1]
        self.resultwindow.insert(0, y)

    def calculate(self):
        x = self.resultwindow.get()
        ans = eval(x)
        self.resultwindow.delete(0, 'end')
        self.resultwindow.insert(0, ans)

if __name__ == "__main__":
    calc()