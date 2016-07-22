from termcolor import cprint
from models import Player
import views

def gender(self):
  while True:
    choice = input("What is your gender?\n[M]ale\n[F]emale\n[O]ther\n").lower()
    if choice in Player.genders:
      return choice

def name():
  while True:  
    choice = input("Do you want to change your name?\n[Y]es\n[N]o\n")
    if choice.lower() == 'y':
      while True:
        print("What should we call you?")
        cprint("[N]ever mind", "grey")
        choice = input()
        if choice.lower() == 'n':
          return "Irí"
        elif choice != "":
          return choice
        else:
          print(views.try_again)
    elif choice.lower() == 'n':
      return "Irí"
    else:
      print(views.try_again)
    # choice = input("What should we call you?\n")
    
intro = ["Elder Saerl: The world of Pana is dying, young one.", "Elder Saerl: For centuries we have endured, under the watchful shadow of the Wellspring Primus. One of the last true settlements, reduced to a mere shadow of its former self. Long before you were born, we knew even the raw natural power of the Wellspring would eventually wane, and leave us with nothing but dust.", "Elder Saerl: But the day you were born, when your mother...", "Elder Saerl: You were born with a gift, Irí. Your vitality will drive away the decay which plagues us. I have already sent word to Ols; this is something worth traversing the continent for.", "Elder Saerl: Shh, hush now. You will share your light with the world...I just pray it's not too late."]

try_again = "Sorry, I didn't understand that."
# def intro(self):
#   #GameState.location = "Lalivero"
#   print('''This is the world of Weyard. For an age the world has been at peace, with magic and the djinn in harmony with the people. This peace has been upheld thanks to the tireless efforts of a nameless watchman. The mantle has been passed from generation to generation in relative secrecy. All anyone knows, or really cares to know, is that the watchman is the strongest in the land, able to keep the djinn themselves in line, and is responsible for the peace that all enjoy.

# Parents tell their children stories of a mythical time before the watchman when monsters roamed the countryside and djinn, who controlled one region or another, fought bloody wars. Of course, this was long before anyone can remember and many wonder if it wasn't always like it is now.

# But something has changed. The djinn have become restless, seizing towns throughout the world. They have created new monsters to terrorize travelers, destroying trade routes, and isolating the people in ways they haven't seen this age.

# But hope remains. The people of Lalivero have seen {do} watching from atop the Babi Lighthouse, contemplating his course of action...'''.format(**self.gender))
#   return input("What is the watchman's name?\n")