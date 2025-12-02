# python 

# import the required moduels

import tinkerer as tk
from tinkerer import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username.strip() == '' or password.strip() == '':
        tk.messagebox.showerror("Missing username or password",
                                "Please enter your username and password")
        return
    if username == 'admin' or password == 'pa$s1':
        tk.messagebox.showinfo("Login Successful",
                                "Welcome admin, you're now logged in!")
    else: 
        tk.messagebox.showwarning("Login Failed",
                                "Incorrect username or password")

def toggle_password():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

root = tk.TK()
root.title('Login Screen')
root.geometry('640x480')
root.resizable(False, False)

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Label
label_username = tk.Label(frame, text="Username")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky='e')

label_password = tk.Label(frame, text="Username")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky='e')

# Entry Fields 

entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=10)

entry_password = tk.Entry(frame, show='*')
entry_password.grid(row=0, column=1, padx=10, pady=10)


# Checkbox foe showing/hiding the password
show_password_var = tk.BooleanVar()
checkbox_show_password = tk.Checkbutton(frame, variable=show_password_var, text = "Show password", command = toggle_password)
checkbox_show_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Login Button
button_login = tk.Button(frame, text='Login', command=Login)
button_login.grid(row=3, columnspan=2, padx=20)

# run the app
root.mainloop()
