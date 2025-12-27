from tkinter import *

def convert_miles_to_km():
    given_miles = float(miles_entry.get())
    converted_kms = round(1.60934 * given_miles, 2)
    result_label.config(text=str(converted_kms))

window = Tk()
window.minsize(width=200, height=100)
window.title('Miles to Kilometers Converter')
window.config(padx=20, pady=20)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

miles_entry = Entry(width=5)
miles_entry.config()
miles_entry.grid(row=0, column=1)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

result_label = Label(text='0')
result_label.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=convert_miles_to_km)
calculate_button.grid(row=3, column=1)

window.mainloop()
