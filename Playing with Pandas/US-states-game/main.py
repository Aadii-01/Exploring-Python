import turtle
import pandas
screen = turtle.Screen()
turtle.title("U.S. States Game")
image = "blank_states_img.gif"          #Turtle only allows gif as input , not jpg,jpeg or any other
screen.addshape(image)
turtle.shape(image)

"""TO TAKE THE RESPONSE FROM THE SCREEN AND RECORD THE COORDINATES"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()          #List of all the states
guessed_state = []                         #List on un-guessed states after leaving
total_states = 50                          #total states in the country
while len(guessed_state) < total_states:
    answer_state = screen.textinput(title= f"{len(guessed_state)}/50 states correct", prompt = " What's another state's name?").title()

    """If Exit is entered as input, will generate a new csv file of un-guessed states and break loop"""
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    """Checks the authenticity of the answered state"""
    if answer_state in all_states :
        guessed_state.append(answer_state)
        nav = turtle.Turtle()                                   #Our navigation pointer moves over map as per correct input
        nav.hideturtle()                                        #We don't want to show our pointer, do we ?
        nav.penup()                                             #So that our nav ptr doesn't spread the ink :)
        state_data = data[data.state == answer_state]           #Check condition if answered state is in data state list
        nav.goto(state_data.x.item(), state_data.y.item())      #Goes on the specified coordinate and writes the name
        nav.write(answer_state)
