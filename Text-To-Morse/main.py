morse_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
    }

user_input = input("Type out a word: ").upper()
converted_text = ""


for n in user_input:
    if n in morse_alphabet:
        converted_text = converted_text + " " + morse_alphabet[n]
    elif n == " ":
        converted_text = converted_text + '/'
    else:
        print('Invalid input')
        break
print(converted_text)