from sqlalchemy import *
from logic import Player
from sqlalchemy.ext.declarative import declarative_base

Base = declaritive_base()

engine = create_engine("sqlite:///app.db")
metadata = MetaData()
metadata.bind = engine
player_table = Table("player", metadata, autoload = True)

player = engine.execute(
        player_table.select().where(player_table.c.id == 1)
)

forrest = Player()

print(player)