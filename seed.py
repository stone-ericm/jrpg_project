from sqlalchemy import create_engine, Table, Column, Enum, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint, Boolean

engine = create_engine('sqlite:///app.db')

metadata = MetaData()

player = Table('player', metadata,
    Column('gender', Enum('m', 'f', 'o')),
    Column('name', String),
    Column('hp', Integer),
    Column('mp', Integer),
    Column('strength', Integer),
    Column('fortitude', Integer),
    Column('agility', Integer),
    Column('skill_points', Integer),
    Column('gold', Integer),
    Column('poisoned', Boolean)
    )

skills = Table('skills', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('purchase_cost', Integer),
    Column('use_cost', Integer),
    Column('damage_heal', Integer),
    Column('poisonous', Boolean)
    )

items = Table('items', metadata,
    Column('id', Integer, primary_key=True),
    Column('buy_value', Integer),
    Column('sell_value', Integer),
    Column('name', String),
    Column('itype', Enum('weapon', 'healing_item', 'head', 'chest', 'legs', 'feet', 'key_items', 'repel')),
    Column('attack_mod', Integer),
    Column('defense_mod', Integer),
    Column('agility_mod', Integer),
    Column('recov_amnt', Integer),
    Column('hp_mp', Enum('hp', 'mp')),
    Column('enemy_id', Integer, ForeignKey('enemies.id'))
    )
    
enemies = Table('enemies', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('hp', Integer),
    Column('mp', Integer),
    Column('strength', Integer),
    Column('fortitude', Integer),
    Column('agility', Integer),
    Column('poisoned', Boolean),
    Column('gold', Integer),
    Column('boss', Boolean)
)

allies = Table('allies', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('hp', Integer),
    Column('mp', Integer),
    Column('strength', Integer),
    Column('fortitude', Integer),
    Column('agility', Integer),
    Column('poisoned', Boolean)
)

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

metadata.create_all(engine)

## TODO
## tables for items, spells, enemies, shop inventories, user save file