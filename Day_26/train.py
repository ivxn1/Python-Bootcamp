from tkinter import *

from PIL.ImageOps import expand
def button_clicked():
    entered_text = entry.get()
    label['text'] = entered_text

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window['padx'] = 200
window['pady'] = 300

label = Label(text="I am a label", font=('Times New Roman', 24, 'bold'))
label.grid(row=0, column=0)
label.config(padx=30)
label.config(pady=40)

label['text'] = 'I am just a text'


button = Button(text="i AM A button", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="NEW BUTTON")
new_button.grid(row=0, column=2)

entry = Entry(width=30)
entry.grid(row=3, column=3)


window.mainloop()
