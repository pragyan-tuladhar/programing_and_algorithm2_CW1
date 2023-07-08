import requests
from tkinter import *
from tkinter import messagebox


def enumerate_website():
    url = url_entry.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response_text = response.text
            # Perform desired web enumeration tasks here
            result_text.delete(1.0, END)  # Clear previous results
            result_text.insert(END, response_text)
        else:
            messagebox.showerror("Error", "Unable to retrieve data from the website.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))


# Create the main window
window = Tk()
window.title("Web Enumeration Tool")

# Create Menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.quit)

# Create URL entry field
url_label = Label(window, text="URL:")
url_label.pack()

url_entry = Entry(window)
url_entry.pack()

# Create Enumerate button
enumerate_button = Button(window, text="Enumerate", command=enumerate_website)
enumerate_button.pack()

# Create result text box
result_label = Label(window, text="Result:")
result_label.pack()

result_text = Text(window)
result_text.pack()

# Create scrollbar for the result text box
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

# Create radio buttons
radio_var = IntVar()

radio_frame = Frame(window)
radio_frame.pack()

radio_label = Label(radio_frame, text="Enumeration Type:")
radio_label.pack(anchor=W)

radio1 = Radiobutton(radio_frame, text="Type 1", variable=radio_var, value=1)
radio1.pack(anchor=W)

radio2 = Radiobutton(radio_frame, text="Type 2", variable=radio_var, value=2)
radio2.pack(anchor=W)

radio3 = Radiobutton(radio_frame, text="Type 3", variable=radio_var, value=3)
radio3.pack(anchor=W)

# Start the GUI event loop
window.mainloop()
