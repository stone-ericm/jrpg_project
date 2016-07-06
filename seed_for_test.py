from sqlalchemy import MetaData, insert, create_engine, Table

engine = create_engine("sqlite:///app.db")
engine.echo = True
conn = engine.connect()
metadata = MetaData()
metadata.bind = engine

player_table = Table("player", metadata, autoload=True)

add_player = player_table.insert().values(
    gender = "m",
    name = "Forrest",
    hp = 50,
    mp = 50,
    strength = 50,
    fortitude = 50,
    agility = 50,
    skill_points = 20,
    gold = 20,
    poisoned = False
    )

result = conn.execute(add_player)

enemy_table = Table("enemies", metadata, autoload=True)

add_enemy = enemy_table.insert().values(
    name = "Rat",
    hp = 10,
    mp = 0,
    strength = 5,
    fortitude = 5,
    agility = 2,
    poisoned = False,
    gold = 13,
    boss = False
    )
    
result = conn.execute(add_enemy)