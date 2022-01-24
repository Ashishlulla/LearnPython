# importing tkinter module
import tkinter as tk
from tkinter import ttk  # importing ttk (Tkinter Sub Module)
from csv import DictWriter
import os

# start line
window = tk.Tk()

# title method
window.title("tkinter")

# Create Labels

name_label = ttk.Label(window, text="Name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(window, text="Email : ")
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(window, text="Age : ")
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(window, text="Gender : ")
gender_label.grid(row=3, column=0, sticky=tk.W)

# Create Entry Box

name_var = tk.StringVar()
name_entry = ttk.Entry(window, width=16, textvariable=name_var)
name_entry.grid(row=0, column=1)
name_entry.focus()

email_var = tk.StringVar()
email_entry = ttk.Entry(window, width=16, textvariable=email_var)
email_entry.grid(row=1, column=1)

age_var = tk.StringVar()
age_entry = ttk.Entry(window, width=16, textvariable=age_var)
age_entry.grid(row=2, column=1)

# Combo Box:

gender_var = tk.StringVar()
gender = ttk.Combobox(window, width=14, textvariable=gender_var, state='readonly')
gender["values"] = ("Male", "Female", "Other")
gender.current(0)
gender.grid(row=3, column=1)

# Radio Button

user_type = tk.StringVar()
radio_btn1 = ttk.Radiobutton(window, text="Student", value="Student", variable=user_type)
radio_btn1.grid(row=4, column=0)

radio_btn2 = ttk.Radiobutton(window, text="Teacher", value="Teacher", variable=user_type)
radio_btn2.grid(row=4, column=1)

# Check Button:
chk_var = tk.IntVar()
chk_btn = ttk.Checkbutton(window, text="check if you want to subscribe to our news letter", variable=chk_var)
chk_btn.grid(row=5, columnspan=5)


# Create  Button

# Write to text file:
# def action():
#     username = name_var.get()
#     user_age = age_var.get()
#     user_email = email_var.get()
#     user_gender = gender_var.get()
#     type = user_type.get()
#     if chk_var.get() ==0:
#         subscribed = "No"
#     else:
#         subscribed = "Yes"
#
#     with open("file.txt", "a") as f:
#         f.write(f"{username},{user_age},{user_gender},{type},{subscribed}")
#
#     name_entry.delete(0, tk.END)
#     age_entry.delete(0, tk.END)
#     email_entry.delete(0, tk.END)

# Write to csv file
def action():
    username = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    u_type = user_type.get()
    if chk_var.get() == 0:
        subscribed = "No"
    else:
        subscribed = "Yes"

    with open("file1.csv", "a", newline="") as f:
        dict_writer = DictWriter(f, fieldnames=['Username', 'User_email', "User_age", "User_Gender", "User_type",
                                                "Subscribed"])
        if os.stat('file1.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Username': username,
            'User_email': user_email,
            "User_age": user_age,
            "User_Gender": user_gender,
            "User_type": u_type,
            "Subscribed": subscribed
        })

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


submit = tk.Button(window, text="Submit", command=action)
submit.grid(row=6, column=0)

# End Line
window.mainloop()
