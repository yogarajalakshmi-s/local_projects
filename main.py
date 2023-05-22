import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # Pandas Dataframe Iteration
word = input("Enter a word: ").upper()
new_list = [nato_phonetics_dict[letter] for letter in word]
print(new_list)
