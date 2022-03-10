import turtle 
import pandas
FONT = ("Arial", 8, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#Get every state's coordinates.
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()


    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") 
        break

    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_text = turtle.Turtle()
        state_text.hideturtle()  
        state_text.penup()
        state_row = data[data["state"] == answer_state]
        state_x = int(state_row["x"])
        state_y = int(state_row["y"])
        state_text.goto(state_x, state_y)
        state_text.write(answer_state, font=FONT)