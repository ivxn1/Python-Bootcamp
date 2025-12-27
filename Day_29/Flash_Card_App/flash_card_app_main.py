import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Open either edited or original dictionary file to retrieve all words
try:
    words_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("./data/french_words.csv")
    words_dictionary = pandas.DataFrame.to_dict(original_words, orient='records')
else:
    words_dictionary = pandas.DataFrame.to_dict(words_data, orient='records')
current_card = {}

# Function to generate and display a new French word flashcard
# - Cancels any previously scheduled card flip to avoid overlap
# - Selects a random word pair (French-English) from the words_dictionary
# - Updates the flashcard to show the French side of the new word
# - Resets the visual elements (language label and word) to match the new card
# - Schedules the card to flip automatically after 3 seconds to show the English translation
def generate_word():
    global current_card, timer
    window.after_cancel(timer)

    random_card = random.choice(words_dictionary)
    current_card = random_card
    current_french = current_card['French']

    canvas.itemconfig(front_screen, image=front_image)
    canvas.itemconfig(language_label, text="French", fill='black')
    canvas.itemconfig(foreign_word_label, text=current_french, fill='black')
    timer = window.after(3000, flip_card)

# Flips the flashcard to show the English translation of the current word
# - Changes the card image to the back
# - Updates the language label to "English"
# - Displays the English word from the current card
def flip_card():
    global current_card
    current_english = current_card['English']
    canvas.itemconfig(language_label, text="English", fill='white')
    canvas.itemconfig(front_screen, image=back_image)
    canvas.itemconfig(foreign_word_label, text=current_english, fill='white')

# Marks the current word as known and removes it from the learning list
# - Removes the word from the in-memory list
# - Saves the updated list to a CSV file for persistence
# - Loads a new word by calling generate_word()
def word_is_known():
    global current_card
    words_dictionary.remove(current_card)
    fixed_data = pandas.DataFrame(words_dictionary)
    fixed_data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# ---------------------------- GUI SETUP ---------------------------- #
# Initializes the birthday_wisher_main.py window and configures the layout and visuals:
# - Sets window title, size, padding, and background color
# - Loads card images (front and back), and tick/cross button icons
# - Creates a canvas to display the flashcard and text elements
# - Adds two buttons for user feedback (right = known, wrong = skip)
# - Starts the app by generating the first word and running the birthday_wisher_main.py loop
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, flip_card)

tick_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
front_screen = canvas.create_image(400, 263, image=front_image)

language_label = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'), fill='black')
foreign_word_label = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'), fill='black')

wrong_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=generate_word)
wrong_button.grid(row=1, column=0)

correct_button = Button(image=tick_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=word_is_known)
correct_button.grid(row=1, column=1)

generate_word()
window.mainloop()