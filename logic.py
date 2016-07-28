from models import *
import os
if not os.path.isfile("app.db"):
  Base.metadata.create_all(engine)
  import seed_for_test
import views
# from battle import *
from termcolor import colored, cprint
import time
import battle
import demo

Session = alchemy.orm.sessionmaker(bind=engine)
session = Session()

class GameState:
  
  def __init__(self):
      
    save_files = session.query(Player).filter_by(id=1).all()
    # save_files = []
    while True:  
      print("[N]ew Game")
      if save_files:
        print("[C]ontinue")
      else:
        cprint("[C]ontinue", "grey")
      choice = input()
      if choice.lower() == 'n':
        for each in views.intro:
          print (each)
          print(views.cont)
          input()
        print("Do-do-do-do-da-dodo")
        print("Not Golden Sun")
        new = Player(gender = views.gender(self),
                    name = views.name(),
                    level = 10,
                    hp = 50,
                    max_hp = 50,
                    mp = 9,
                    max_mp = 9,
                    strength = 50,
                    fortitude = 50,
                    agility = 45,
                    skill_points = 0,
                    gold = 20,
                    poisoned = False
        )
        skills = []
        print("*TEST*"*5, "\nWhat skills do you want?")
        for each in session.query(Skill).all():
          while True:
            # output = each.name, str(index)
            print(each.name, "\ny/n")
            choice = input()
            if choice == 'y':
              skills.append(each)
              break
            elif choice == 'n':
              break
        break
      elif choice.lower() == 'c':
        if save_files:
          for index, each in enumerate(save_files, start=1):
            print(index, each.name)
          choice = input()
          if int(choice) in range(1, len(save_files)+1):
            new = save_files[int(choice)-1]
            skills = [session.query(Skill).filter_by(id = each.skill_id).all()[0] for each in session.query(SkillOwnership).filter_by(player_id = new.id).all()]
            break
        else:
          print("You have no saved games.")
          input(views.cont)
      else:
        print(views.try_again)
        input(views.cont)
    choice = demo.run(new, skills)
    if choice == 'battle':
      battle.Battle(new, skills).encounter()
      
      # town.town(new)
