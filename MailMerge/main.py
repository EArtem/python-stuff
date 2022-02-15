
with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.read().split('\n')

with open('Input/Letters/starting_letter.txt', 'r') as starting_letter_file:
    starting_letter = starting_letter_file.read()

for name in names:
    path = f'Output/ReadyToSend/{name}.txt'
    starting_letter = starting_letter.replace('[name]', name)
    with open(path, mode='w') as completed_letter:
        completed_letter.write(starting_letter)
