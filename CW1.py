import socket
import sys
from tkinter import *

# GUI layout
root = Tk()
root.geometry("600x600")
root.tk_setPalette(background="#A83020", activeBackground="pink", foreground="White", activeForeground="red")
root.title("PORT SCANNER")

# Labels
Label(text="PORT SCANNER", fg="White", font=("Jokerman", 44, "bold")).pack()
Label(text="Enter the ip of the target: ", pady=10, fg="White", font=("Times Roman Roman", 22, "bold")).pack()
Label(text="Enter the lower limit of port: ", pady=10, fg="White", font=("Times Roman Roman", 22, "bold")).pack()
Label(text="Enter the upper limit of port: ", pady=10, fg="White", font=("Times Roman Roman", 22, "bold")).pack()
# Entry boxes
ip = IntVar()
port1 = IntVar()
port2 = IntVar()

Entry(root, textvariable=ip).pack()
Entry(root, textvariable=port1).pack()
Entry(root, textvariable=port2).pack()


# Menu
def helps():
    print("This is the Help Menu")


my_menu = Menu(root)
my_menu.add_command(label="Help", command=helps)


root.config(m=my_menu)


# Buttons
Button(text="Start Scan", pady=5,).pack()
Button(text="  Save  ", pady=5,).pack()
Button(text="   Exit   ", pady=5,).pack()

root.mainloop()
