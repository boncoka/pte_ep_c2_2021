from easygui import *


user_response = msgbox("Hello there!", title="Hello", ok_button="Hi", image="python_logo.png")
print(user_response)
flavor = buttonbox("What is your favourite ice cream flavor?", title="Icecream",
                           choices=['Vanilla', 'Chocolate', 'Strawberry', 'Cherry'],
                           default_choice="Vanilla[1]")
msgbox("You picked " + flavor)

flavor = choicebox("What is your favourite ice cream flavor?", title="Icecream2",
                   choices=['Vanilla', 'Chocolate', 'Strawberry', 'Cherry'], preselect=1,)
msgbox("You picked " + flavor)

flavor = enterbox("What is your favourite ice cream flavor?", title="Icecream3", default="Korte", image="python_logo.png")
if flavor is not None:
    msgbox("You picked " + flavor)
else:
    print("Kilepett a felhasznalo")