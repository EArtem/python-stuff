import turtle
import pandas as pd
import state_name
BACKGROUND = '/Users/artemevgrafov/PycharmProjects/python-stuff/data/blank_states_img.gif'
ALL_STATES = '/Users/artemevgrafov/PycharmProjects/python-stuff/data/50_states.csv'


screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(BACKGROUND)
turtle.shape(BACKGROUND)
is_game_on = True

data = pd.read_csv(ALL_STATES)
guessed_states = []

'''
[state for state in list_of_all_states if
                              all(guessed_state not in state for guessed_state in guessed_states)]
'''

while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='What another state\'s '
                                                                                             'name?').title()
    get_data = data.get(data.state == answer_state)

    if answer_state == 'Exit':
        list_of_all_states = data.state.to_list()
        not_guessed_states = [state for state in list_of_all_states if state not in guessed_states]
        df = pd.DataFrame(not_guessed_states, columns=['state'])
        df.to_csv('/Users/artemevgrafov/PycharmProjects/python-stuff/data/not_guessed_state.csv', index=False, mode='w')
        break

    if not get_data.empty and answer_state not in guessed_states:
        x = get_data.x.to_list()
        y = get_data.y.to_list()
        name_of_the_state = get_data.state.to_list()
        print(name_of_the_state)
        state = state_name.StateName()
        state.place_state_name_on_map(x, y)
        state.name_state(name_of_the_state)
        guessed_states.append(name_of_the_state[0])
        print(guessed_states)
