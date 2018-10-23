from tkinter import *
from tkinter import ttk

class Calculator:

        def_value = 0.0

        add_triggered = False 
        sub_triggered = False
        times_triggered = False
        divide_triggered = False

        def AC_press(self, AC):

            self.add_triggered = False 
            self.sub_triggered = False
            self.times_triggered = False
            self.divide_triggered = False
            
            self.number_entry.delete(0,"end")

        def number_press(self, value):
            
            entry_val = self.number_entry.get()
            entry_val += value 

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0,entry_val)

        def isFloat(self, str_val):
            #tries to convert passed value to float, if success, return true, if Vlaue Error: return false
            try:
                float(str_val)
                return True
            except ValueError:
                return False
        
        def math_press(self, value):
            if self.isFloat(str(self.number_entry.get())):
                self.add_triggered = False 
                self.sub_triggered = False
                self.times_triggered = False
                self.divide_triggered = False

                self.calc_value = float(self.entry_value.get())

                if value == "/":
                    self.divide_triggered = True
                elif value == "*":
                    self.times_triggered = True
                elif value == "+":
                    self.add_triggered = True
                elif value == "-":
                    self.sub_triggered = True

                self.number_entry.delete(0, "end")

        def equal_press(self, equal):
            if self.add_triggered:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_triggered:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.divide_triggered:
                solution = self.calc_value / float(self.entry_value.get())
            elif self.times_triggered:
                solution = self.calc_value * float(self.entry_value.get())

            self.number_entry.delete(0,"end")

            self.number_entry.insert(0,solution)



        def __init__(self, root):

            self.entry_value = StringVar(root, value = "")

            #sets title of the app
            root.title("Python_Calculator")
            
            #hard codes the width height of the app 
            root.geometry("600x600")
            
            #size unchangable by user
            root.resizable(width = False, height= False)
            
            #sets style for the Buttons and our Entry
            style = ttk.Style()
            style.configure("TButton", font = "Serif 15", padding = 10)
            style.configure("TEntry", font = "Serif 18", padding = 10)

            #sets values of number entry and loc
            self.number_entry = ttk.Entry(root, textvariable = self.entry_value, width = 50)
            self.number_entry.grid(row = 0, columnspan = 4)

            #sets button top row button style, location and events.
            self.button7 = ttk.Button(root, text = "7", command = lambda: self.number_press("7")).grid(row = 1, column =0)
            self.button8 = ttk.Button(root, text = "8", command = lambda: self.number_press("8")).grid(row = 1, column =1)
            self.button9 = ttk.Button(root, text = "9", command = lambda: self.number_press("9")).grid(row = 1, column =2)
            self.button_divide = ttk.Button(root, text = "/", command = lambda: self.math_press("/")).grid(row = 1, column =3)

            #2nd row buttons
            self.button4 = ttk.Button(root, text = "4", command = lambda: self.number_press("4")).grid(row = 2, column =0)
            self.button5 = ttk.Button(root, text = "5", command = lambda: self.number_press("5")).grid(row = 2, column =1)
            self.button6 = ttk.Button(root, text = "6", command = lambda: self.number_press("6")).grid(row = 2, column =2)
            self.button_times = ttk.Button(root, text = "*", command = lambda: self.math_press("*")).grid(row = 2, column =3)

            #3rd row buttons
            self.button1 = ttk.Button(root, text = "1", command = lambda: self.number_press("1")).grid(row = 3, column =0)
            self.button2 = ttk.Button(root, text = "2", command = lambda: self.number_press("2")).grid(row = 3, column =1)
            self.button3 = ttk.Button(root, text = "3", command = lambda: self.number_press("3")).grid(row = 3, column =2)
            self.button_add = ttk.Button(root, text = "+", command = lambda: self.math_press("+")).grid(row = 3, column =3)

            #4th row buttons
            self.button_AC = ttk.Button(root, text = "AC", command = lambda: self.AC_press("AC")).grid(row = 4, column =0)
            self.button0 = ttk.Button(root, text = "0", command = lambda: self.number_press("0")).grid(row = 4, column =1)
            self.button_equal = ttk.Button(root, text = "=", command = lambda: self.equal_press("=")).grid(row = 4, column =2)
            self.button_sub = ttk.Button(root, text = "-", command = lambda: self.math_press("-")).grid(row = 4, column =3)


root = Tk()
calc = Calculator(root)

root.mainloop()
