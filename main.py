from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title('U.S States Game')
screen.addshape('blank_states_img.gif')

image = Turtle()
image.shape('blank_states_img.gif')

states = pd.read_csv('50_states.csv')
# print(states)

list_states = states['state'].to_list()
# print(list_states)
guesses_states = []
guess = 0
game_over = False
while guess<50:
    
    answer_state = (screen.textinput(title=f'Guess the State {guess}/50 ', prompt="What's another state's name")).title()
    if answer_state == 'Exit': 
        # missing_states = []
        # for state in list_states:
        #     if state not in  guesses_states:
        #         missing_states.append(state)
        missing_states = [ state for state in list_states if state not in guesses_states]
        df = pd.DataFrame(missing_states)
        df.to_csv('States_to_learn.csv')
        break
    
    if answer_state in list_states:
        state_info = states[states['state'] == answer_state]
        guesses_states.append(answer_state)
        x_coord = int(state_info.x)
        # print(x_coord)
        # print(type(x_coord))
        y_coord = int(state_info.y)
        # print(y_coord)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x_coord, y_coord)
        turtle.write(answer_state, align= 'center', font= ('courier', 8, 'normal')) #tambien se podria colocar state_info.state.item()
        guess += 1
        

# screen.exitonclick()

