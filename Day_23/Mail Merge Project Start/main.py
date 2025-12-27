#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    names_list = [n.strip() for n in names.readlines()]


with open("./Input/Letters/starting_letter.txt") as template:
    message = template.read()

for n in names_list:
    new_message = message.replace("[name]", n)
    with open(f"./Output/ReadyToSend/message_{n}", mode='w') as file:
        file.write(new_message)
