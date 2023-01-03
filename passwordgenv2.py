# Importing random, pyperclip, and Tkinter modules
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function for password generation


def low():
	entry.delete(0, END)

	# Get the length of password
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	# If strength selected is low
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	# If strength selected is medium
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	# If strength selected is strong
	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")


# Function for generation of password
def generate():
	password1 = low()
	entry.insert(10, password1)


# Function for copying password to clipboard
def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


# Main Function

# Create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Random Password Generator")

# Create label and entry to show password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# Create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)

# Create Buttons Copy which will copy password to clipboard and generate which will generate the password
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

# Radio Buttons for deciding the strength of the password, default strength is medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

# Start the GUI
root.mainloop()
