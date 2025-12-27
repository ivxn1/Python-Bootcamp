import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet_codes_map = {row.letter:row.code for (index, row) in nato_data.iterrows()}

def generate_spelling():
    input_word = input("Please, enter a word: ").upper()

    try:
        spelled_word = [nato_alphabet_codes_map[l] for l in input_word]
    except KeyError:
        print("Sorry, you have entered an illegal character. Please try again!")
        generate_spelling()
    else:
        print(spelled_word)

generate_spelling()