# Morse code generator
CODES = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', '0': '-----'}


str_input = input("Enter something to get the Morse code: ").upper()
morse_code = ""
for char in str_input:
    if char in CODES:
        morse_code += f"{CODES[char]} "

# morse_code = [f"{CODES[char]} " for char in str_input if char in CODES]

print(f"Morse code of {str_input}: {morse_code}")
