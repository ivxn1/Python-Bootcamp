from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def search_account():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            email_username = data[website]['email_username']
            password = data[website]['password']
    except KeyError:
        messagebox.showerror(title="Oops", message="Please make sure you search for an existing website account!")
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found error!")
    else:
        messagebox.showinfo(message=f"Details for {website}\n\nEmail: {email_username}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
        "email_username": email_username,
        "password": password
        }
    }

    if website == '' or password == '' or email_username == '':
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!")
        return

    user_agrees = messagebox.askokcancel(title=f"{website}", message=F"These are the entered details:\n\n"
                                                                     F"Email: {email_username}\n"
                                                                     F"Password: {password}\n\n"
                                                                     F"Are you sure you want to add those credentials?")
    if user_agrees:
        try:
            with open("data.json", 'r') as datafile:
                data = json.load(datafile)

        except FileNotFoundError:
            with open("data.json", 'w') as datafile:
                json.dump(new_data, datafile, indent=4)

        else:
            data.update(new_data)
            with open("data.json", 'w') as datafile:
                json.dump(data, datafile, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(bg="white", padx=50, pady=50)

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)

image = PhotoImage(file='logo.png')

canvas.create_image(130, 95, image=image)

website_label = Label(text="Website:", bg='white', fg='black')
website_label.grid(row=1, column=0)

website_entry = Entry(width=21, bg='white', highlightthickness=0, fg='black')
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_label = Label(text="Email/Username:", bg='white', fg='black')
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=38, bg='white', highlightthickness=0, fg='black')
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "ivxn.zhelev@gmail.com")

password_label = Label(text="Password:", bg='white', fg='black')
password_label.grid(row=3, column=0)

password_entry = Entry(width=21, bg='white', highlightthickness=0, fg='black')
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', bg='white', highlightthickness=0,
                                  highlightbackground='white', width=13, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightbackground='white', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_account_button = Button(text='Search', highlightbackground='white', width=13, bg='white', highlightthickness=0, command=search_account)
search_account_button.grid(row=1, column=2)

window.mainloop()