from termcolor import cprint, colored
from models import Player
import views

def gender(self):
  while True:
    choice = input("What is your gender?\n[M]ale\n[F]emale\n[O]ther\n").lower()
    if choice in Player.genders:
      return choice
    else:
      print(try_again)
      input(views.cont)

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
      print(try_again)
      input(cont)
    # choice = input("What should we call you?\n")
    
intro = ["Elder Saerl: The world of Pana is dying, young one.", "Elder Saerl: For centuries we have endured, under the watchful shadow of the Wellspring Primus. One of the last true settlements, reduced to a mere shadow of its former self. Long before you were born, we knew even the raw natural power of the Wellspring would eventually wane, and leave us with nothing but dust.", "Elder Saerl: But the day you were born, when your mother...", "Elder Saerl: You were born with a gift, Irí. Your vitality will drive away the decay which plagues us. I have already sent word to Ols; this is something worth traversing the continent for.", "Elder Saerl: Shh, hush now. You will share your light with the world...I just pray it's not too late."]

try_again = "Sorry, I didn't understand that."

sixteen_years_later = ["Sixteen Years Later", "Elder Saerl: I worry, Jou. Irí is not yet ready! We need more time to train, more time to study...","Elder Jou: We cannot wait any longer! Haven't you seen the signs? We must have a few months left, if that!", "Elder Saerl:  ...", "Elder Saerl: Alright.", "Elder Saerl: It's time to wake up, young one. It appears the time to act has come sooner than we predicted.", "You wake up in your room. The two great elders of your village, Saerl and Jou, stand over your bed. They both look concerned, and Jou looks rather impatient."]

cont = colored("[press Enter to continue]", "grey")