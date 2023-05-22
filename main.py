import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

count = 0
states_data = pandas.read_csv('50_states.csv')
us_states = states_data['state'].to_list()
correct_guesses = []
while len(correct_guesses) < 50:

    state_guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt='Name a state').title()

    if state_guess == 'Exit':
        states_to_learn = [state for state in us_states if state not in correct_guesses]
        states_list = pandas.DataFrame(states_to_learn)
        states_list.to_csv('states_to_learn.csv')
        break

    if state_guess not in correct_guesses and state_guess in us_states:
        correct_guesses.append(state_guess)
        guessed_state_data = states_data[states_data.state == state_guess]
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(int(guessed_state_data.x), int(guessed_state_data.y))
        new_state.write(state_guess, True, align='center')
