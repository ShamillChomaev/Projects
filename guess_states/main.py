import turtle
import pandas

screen = turtle.Screen()
screen.title("USA states")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_list = []
while len(guess_list) <50:
    answer_state = screen.textinput(title=f"{len(guess_list)}/50 Correct", prompt="What is the next state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in guess_list if state not in guess_list]
        for state in all_states:
            if state not in guess_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed_states.csv")
        break

    if answer_state in all_states:
        guess_list.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    else:
        answer_state = screen.textinput(title="Guess the state", prompt="What is the next state?")
