from sqlalchemy import create_engine, Table, Column, Enum, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///app.db')

metadata = MetaData()

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True),
    gender = Column(Enum('m', 'f', 'o')),
    name = Column(String),
    hp = Column(Integer),
    mp = Column(Integer),
    strength = Column(Integer),
    fortitude = Column(Integer),
    agility = Column(Integer),
    skill_points = Column(Integer),
    gold = Column(Integer),
    poisoned = Column(Boolean)

class Skill(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True),
    name = Column(String),
    purchase_cost = Column(Integer),
    use_cost = Column(Integer),
    damage_heal = Column(Integer),
    poisonous = Column(Boolean)

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True),
    buy_value = Column(Integer),
    sell_value = Column(Integer),
    name = Column(String),
    itype = Column(Enum('weapon', 'healing_item', 'head', 'chest', 'legs', 'feet', 'key_items', 'repel')),
    attack_mod = Column(Integer),
    defense_mod = Column(Integer),
    agility_mod = Column(Integer),
    recov_amnt = Column(Integer),
    hp_mp = Column(Enum('hp', 'mp')),
    enemy_id = Column(Integer, ForeignKey('enemies.id'))

class Enemy(Base):
    __tablename__ = 'enemies'
    
    id = Column(Integer, primary_key=True),
    name = Column(String),
    hp = Column(Integer),
    mp = Column(Integer),
    strength = Column(Integer),
    fortitude = Column(Integer),
    agility = Column(Integer),
    poisoned = Column(Boolean),
    gold = Column(Integer),
    boss = Column(Boolean)

class Ally(Base):
    __tablename__ = 'allies'
    
    id = Column(Integer, primary_key=True),
    name = Column(String),
    hp = Column(Integer),
    mp = Column(Integer),
    strength = Column(Integer),
    fortitude = Column(Integer),
    agility = Column(Integer),
    poisoned = Column(Boolean)

########################################################
#MERCHANTS
########################################################

merchants = Table('merchants', metadata,
    Column('id', Integer, primary_key=True),
    #sold items insert into delivery
)

delivery = Table('delivery', metadata,
    Column('item_id', Integer, ForeignKey('items.id')),
    Column('merchant_id', Integer, ForeignKey('merchants.id'))
)

########################################################
#DOJO
########################################################

dojo = Table('dojo', metadata,
    Column('id', Integer, primary_key=True),
)

elder = Table('elder', metadata,
    Column('skill_id', Integer, ForeignKey('skills.id')),
    Column('dojo_id', Integer, ForeignKey('dojo.id'))
)

Base.metadata.create_all(engine)

## TODO
## MAKE WORK