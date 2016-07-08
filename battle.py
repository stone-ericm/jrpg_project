import sqlalchemy as alchemy
from models import Player, Enemy, SkillOwnership, Skill
from sqlalchemy.ext.declarative import declarative_base
import random

engine = alchemy.create_engine("sqlite:///app.db")
# Base = declarative_base()
Session = alchemy.orm.sessionmaker(bind=engine)
session = Session()

# player = Player()
metadata = alchemy.MetaData()
metadata.bind = alchemy.engine


player = session.query(Player).filter_by(id=1).all()[0]
enemy = session.query(Enemy).filter_by(name="Rat").all()[0]
skills = [session.query(Skill).filter_by(id = each.skill_id).all()[0] for each in session.query(SkillOwnership).filter_by(player_id = player.id).all()]
skills_dict = {}
player_max_hp = player.hp
for each in skills:
    skills_dict[each.name] = each
skills_list = sorted(list(skills_dict.keys()))
#player = alchemy.engine.execute(
   #     player_table.select().where(player_table.c.id == 1)
#)

# forrest = Player()

# print(player[0].name)
# print(enemy[0].name)
def enemy_attack():
    dodge = input("Enemy {} is about to attack!\nDodge:\n[L]eft\n[R]right\n[U]p\n[D]own\n".format(enemy.name))
    if dodge.lower() == random.choice(['l', 'r', 'u', 'd']):
        print("You narrowly dodged {}'s attack!".format(enemy.name))
    else:
        player.hp -= enemy.strength
        print("You were hit for {} points! {} hp remaining.".format(enemy.strength, player.hp))

def player_attack():
    choice = input("What would you like to do?\n[A]ttack\n[I]tem\n[R]un\n")
    if choice.lower() == 'a':
        for index, skill in enumerate(skills_list, start=1):
            print(index, skill)
        attack = int(input())
        if skills_list[attack-1]:
            damage = skills_dict[skills_list[attack-1]].damage_heal
            if damage > 0:
                enemy.hp -= damage
                print("You hit for {} points! Enemy has {} hp remaining.".format(damage, enemy.hp))
            else:
                player.hp -= damage
                if player.hp > player_max_hp:
                    player.hp = player_max_hp
                print("You healed for {} points! {} hp remaining".format(-damage, player.hp))


def random_encounter():
    print("An enemy {} has appeared!".format(enemy.name))
    # speed check
    if enemy.agility > player.agility:
        while enemy.hp >= 0 and player.hp >= 0:
            enemy_attack()
            player_attack()
        if player.hp <= 0:
            print("You were defeated!")
        elif enemy.hp <= 0:
            print("You defeated {}! {} gold!".format(enemy.name, enemy.gold))
            player.gold += enemy.gold
    
    elif player.agility >= enemy.agility:
        while enemy.hp >= 0 and player.hp >= 0:
            player_attack()
            enemy_attack()
        if player.hp <= 0:
            print("You were defeated!")
        elif enemy.hp <= 0:
            print("You defeated {}! You gained {} gold!".format(enemy.name, enemy.gold))
            player.gold += enemy.gold
            
if __name__ == "__main__":
    random_encounter()
    
##BUGS
# enemy doesn't die at 0
# implement cast costs
# add in basic attack
# add in run
# add in items