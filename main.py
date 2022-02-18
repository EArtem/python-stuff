import pandas as pd


data = pd.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
word = input('Enter a word:\n').upper()
nato_alphabet = [data_dict[letter] for letter in word]
print(nato_alphabet)



