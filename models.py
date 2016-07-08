from sqlalchemy import create_engine, Table, Column, Enum, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
import views, logic


Base = declarative_base()
engine = create_engine('sqlite:///app.db')

metadata = MetaData()

class Player(Base):
    __tablename__ = 'players'
    genders = {
    'm':{"sub":"he", "do":"him", "pos":"his"}, 
    'f':{"sub":"she", "do":"her", "pos":"her"}, 
    'o':{"sub":"they", "do":"them", "pos":"their"}
  }
    
    id = Column(Integer, primary_key=True)
    gender = Column(Enum('m', 'f', 'o'))
    name = Column(String)
    hp = Column(Integer)
    mp = Column(Integer)
    strength = Column(Integer)
    fortitude = Column(Integer)
    agility = Column(Integer)
    skill_points = Column(Integer)
    gold = Column(Integer)
    poisoned = Column(Boolean)
  
    # def gender(self):
    #     choice = views.gender(self)
    #     return self.genders[choice]
    
    # def name(self):
    #     GameState.location = "Lalivero"
    #     return views.intro(self)

class Skill(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    purchase_cost = Column(Integer)
    use_cost = Column(Integer)
    damage_heal = Column(Integer)
    poisonous = Column(Boolean)

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    buy_value = Column(Integer)
    sell_value = Column(Integer)
    name = Column(String)
    itype = Column(Enum('weapon', 'healing_item', 'head', 'chest', 'legs', 'feet', 'key_items', 'repel'))
    attack_mod = Column(Integer)
    defense_mod = Column(Integer)
    agility_mod = Column(Integer)
    recov_amnt = Column(Integer)
    hp_mp = Column(Enum('hp', 'mp'))
    enemy_id = Column(Integer, ForeignKey('enemies.id'))

class Enemy(Base):
    __tablename__ = 'enemies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Integer)
    mp = Column(Integer)
    strength = Column(Integer)
    fortitude = Column(Integer)
    agility = Column(Integer)
    poisoned = Column(Boolean)
    gold = Column(Integer)
    boss = Column(Boolean)
    skill_points = Column(Integer)

class Ally(Base):
    __tablename__ = 'allies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hp = Column(Integer)
    mp = Column(Integer)
    strength = Column(Integer)
    fortitude = Column(Integer)
    agility = Column(Integer)
    poisoned = Column(Boolean)

# FOR USE WITH PLAYERS ONLY. ALLY AND ENEMY MOVESETS WILL BE HARD CODED (7/7/16)
class SkillOwnership(Base):
    __tablename__ = 'skillownership'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))

########################################################
#MERCHANTS
########################################################

class Merchant(Base):
    __tablename__ = 'merchants'
    
    id = Column(Integer, primary_key=True)
    #sold items insert into delivery

class Delivery(Base):
    __tablename__ = 'delivery'
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    merchant_id = Column(Integer, ForeignKey('merchants.id'))

########################################################
#DOJO
########################################################

class Dojo(Base):
    __tablename__ = 'dojos'

    id = Column(Integer, primary_key=True)

class Elder(Base):
    __tablename__ = 'elders'
    
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'))
    dojo_id = Column(Integer, ForeignKey('dojos.id'))


## TODO
## MAKE WORK