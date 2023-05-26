import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Pandas Dataframe Iteration

valid_word = False
while not valid_word:
    word = input("Enter a word: ").upper()
    try:
        new_list = [nato_phonetics_dict[letter] for letter in word]
    except KeyError:
        print("Enter only alphabets!")
    else:
        new_list = [nato_phonetics_dict[letter] for letter in word]
        print(new_list)
        valid_word = True
