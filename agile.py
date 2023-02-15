#requirements gathering
purpose= "A simple calculator performing different functions"
requirements=["numbers","operators","Data Types","statments"]

#Using Scrum Framework
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create display
        self.display = tk.Entry(self.master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        b = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "=", "C", "+"
        ]

        # Create button grid
        row = 1
        col = 0
        for button in b:
            cmd = lambda x=button: self.button_click(x)
            tk.Button(self.master, text=button, width=7, command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    # Button click event
    def click(self, key):
        if key == "C":
            self.display.delete(0, tk.END)
        elif key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

#code and testing of the calculator
def calculator():
    while True:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        op = input("Enter an op (+, -, *, /): ")
        if op == "+":
            output = n1 + n2
            print(f"{n1} + {n2} = {output}")
        elif op == "-":
            output = n1 - n2
            print(f"{n1} - {n2} = {output}")
        elif op == "*":
            output = n1 * n2
            print(f"{n1} * {n2} = {output}")
        elif op == "/":
            if n2 == 0:
                print("Error: division by zero")
            else:
                output = n1 / n2
                print(f"{n1} / {n2} = {output}")
        else:
            print("Error: invalid op")
        choice = input("Do you want to perform another calculation? (yes/no) ")
        if choice.lower() != "yes":
            break

calculator()

