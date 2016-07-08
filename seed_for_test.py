import sqlalchemy as alchemy
from sqlalchemy import MetaData, insert, create_engine, Table
from models import Player, Enemy, Skill, SkillOwnership
engine = create_engine("sqlite:///app.db")
# engine.echo = True
Session = alchemy.orm.sessionmaker(bind=engine)
session = Session()
#conn = engine.connect()
# metadata = MetaData()
# metadata.bind = engine

# player_table = Table("players", metadata, autoload=True)

player_1 = Player(
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

# result = conn.execute(add_player)

# enemy_table = Table("enemies", metadata, autoload=True)

rat = Enemy(
    name = "Rat",
    hp = 10,
    mp = 0,
    strength = 5,
    fortitude = 5,
    agility = 2,
    poisoned = False,
    gold = 13,
    boss = False,
    skill_points = 2
    )
    
# result = conn.execute(add_enemy)

fireball = Skill(
    name = "Fireball",
    purchase_cost = 0,
    use_cost = 2,
    damage_heal = 5,
    poisonous = False
    )

quick_heal = Skill(
    name = "Quick Heal",
    purchase_cost = 0,
    use_cost = 3,
    damage_heal = -10,
    poisonous = False
    )


session.add_all([player_1, rat, fireball, quick_heal])
session.commit()

own_fireball = SkillOwnership(
    player_id = session.query(Player).filter_by(name="Forrest").all()[0].id,
    skill_id = session.query(Skill).filter_by(name="Fireball").all()[0].id
    )

own_quick_heal = SkillOwnership(
    player_id = session.query(Player).filter_by(name="Forrest").all()[0].id,
    skill_id = session.query(Skill).filter_by(name="Quick Heal").all()[0].id
    )

session.add_all([own_fireball, own_quick_heal])
session.commit()