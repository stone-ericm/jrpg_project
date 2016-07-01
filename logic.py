import views

class GameState:
  
  def __init__(self):
    self.player = Player()
    self.location = self.location

class Player:
  genders = {'m':{"sub":"he", "do":"him", "pos":"his"}, 'f':{"sub":"she", "do":"her", "pos":"her"}, 'o':{"sub":"they", "do":"them", "pos":"their"}}

  def __init__(self):
    self.gender = self.gender()
    self.name = self.name()
    self.level = 5
    ##  Equipped items won't appear in the item view. They're stored seperate in the equipped key
    self.items = {"Eqipped":
                   {"Weapon":"Sol Sword",
                    "Head":"",
                    "Chest":"",
                    "Legs":"",
                    "Feet":""},
                  "Weapons":[],
                 }
    self.magic = 
    self.hp = 100
    self.mp = 50
  
  def gender(self):
    choice = views.gender(self)
    return self.genders[choice]
    
  def name(self):
    GameState.location = "Lalivero"
    return views.intro(self)

class Item:
  def __init__(self):
    self.buy_value = self.buy_value
    self.sell_value = self.sell_value
  
  
class Weapon(Item):
  def __init__(self):
    self.attack = self.attack

class Armor(Item):
  def __init__(self):
    self.defense = self.defense

class HealingItem(Item):
  def __init__(self):
    self.heals = self.heals
  
#When I go to a shop what happens?
#Seperate Buy/Sell list by Item type
#Populate list?
  #hard code the items available at each shop
  #Relational database where each shop has a list of items. The items are foreign keys pointing to the items table /w the details
