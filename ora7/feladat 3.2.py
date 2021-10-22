import random
from easygui import *


title = "Szamatalakito"
number = random.randint(1, 100)
back = 6
msgbox("Szia!\n Gondoltam egy szamra 1 es 99 kozott, 6 probad van eltalalni", ok_button="Induljon a jatek", title=title)

won = False
hint = ""
while not won and back > 0:
    guess = enterbox(f"{hint} Meg {back} probalkozasod maradt.\nKerem a tipped:", title=title)
    if guess is not None:
        back -=1
        try:
            guess_number = int(guess)
            if guess_number == number:
                msgbox("Gratulalok, nyertel {} lepesbol".format(6-back), title=title)
                won = True
            elif guess_number < number:
                "Nagyobb szamra gondoltam"
            else:
                "Kisebb szamra gondoltam"
        except ValueError:
            hint = "Hibas bemenet, vesztettel egy eletet"
if not won:
    msgbox("Sajnalom, vesztettel! En a " + str(number) + "gondoltam", title=title)
