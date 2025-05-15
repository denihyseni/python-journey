#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as starting_letter:
    content = starting_letter.read()

with open("Input/Names/invited_names.txt") as names:
    name = names.readlines()

for n in name:
    stripped_n = n.strip("\n")
    new_content = content.replace("[name]",stripped_n)
    with open(f"Output/ReadyToSend/letter_to_{n}",mode="w") as new_letters:
        new_letters.write(new_content)