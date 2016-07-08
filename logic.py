import views, models

class GameState:
  
  def __init__(self):
    self.player = models.Player()
    self.location = self.location

# class Player:
#   genders = {
#     'm':{"sub":"he", "do":"him", "pos":"his"}, 
#     'f':{"sub":"she", "do":"her", "pos":"her"}, 
#     'o':{"sub":"they", "do":"them", "pos":"their"}
#   }

#   def __init__(self):
#     self.gender = self.gender()
#     self.name = self.name()
#     self.hp = 1000
#     self.mp = 50
#     self.strength = 400
#     self.fortitude = 400
#     self.agility = 400
#     self.skill_points = 0
#     self.gold = 0
#     self.poisoned = False
  
#   def gender(self):
#     choice = views.gender(self)
#     return self.genders[choice]
    
#   def name(self):
#     GameState.location = "Lalivero"
#     return views.intro(self)

# class Npc:
#   def __init__(self, **args):
#     self.name = args['name']
#     self.hp = args['hp']
#     self.mp = args['mp']
#     self.strength = args['strength']
#     self.fortitude = args['fortitude']
#     self.agility = args['agility']
#     self.poisoned = args['poisoned']

# class Ally(Npc):
#   def __init__(self):
#     pass

# class Enemy(Npc):
#   def __init__(self, **args):
#     self.gold = args['gold']
#     self.boss = args['boss']

# class Merchant:
#   def __init__(self, **args):
#     self.stock = args['stock']
#     self.dojo = args['dojo']

# class Skill:
#   def __init__(self, **args):
#     self.name = args['name']
#     self.purchase_cost = args['purchase_cost']
#     self.use_cost = args['use_cost']
#     self.damage_heal = args['damage_heal']
#     self.poisonous = args['poisonous']

# class Item:
#   def __init__(self, **args):
#     self.buy_value = args['buy_value']
#     self.sell_value = args['sell_value']
#     self.name = args['name']
#     self.itype = args['itype']
  
# class Weapon(Item):
#   def __init__(self, **args):
#     self.attack_mod = args['attack_mod']
#     self.defense_mod = args['defense_mod']
#     self.agility_mod = args['agility_mod']
    
# class Armor(Item):
#   def __init__(self, **args):
#     self.attack_mod = args['attack_mod']
#     self.defense_mod = args['defense_mod']
#     self.agility_mod = args['agility_mod']
    
# class RecveryItems(Item):
#   def __init__(self, **args):
#     self.recov_amnt = args['recov_amnt']
#     self.hp_mp = args['hp_mp']

#When I go to a shop what happens?
#Seperate Buy/Sell list by Item type
#Populate list?
  #hard code the items available at each shop
  #Relational database where each shop has a list of items. The items are foreign keys pointing to the items table /w the details