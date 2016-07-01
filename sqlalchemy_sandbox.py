from sqlalchemy import create_engine

engine = create_engine("sqlite:///some.db")

with engine.begin() as conn:
    conn.execute('''some SQL code with a variable''', variable="value")
    conn.execute('''some SQL code with another_variable''', another_variable="value1")

##When expecting something back from sql, assign to result object, run result.fetch(all/one)()
result = engine.execute("some SQL")
result.fetchall()

###########################################
#How to create a table
###########################################

from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, Numeric, Enum

metadata = MetaData()
user_table = Table('user', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('fullname', String),
                Column('key', String(50), primary_key=True),
                Column('timestamp', DateTime),
                Column('amount', Numeric(10, 2)),
                Column('type', Enum('a', 'b', 'c'))
             )

user_table.c.name
#Column('name', String(), table=<user>)

user_table.c.keys()
#['id', 'name', 'fullname']

metadata.create_all(engine)

###########################################
#add in some foreign keys
###########################################

from sqlalchemy import ForeignKey

address_table = Table('address', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('email_address', String(100), nullable=False),
                    Column('user_id', Integer, ForeignKey('user.id'))
)

address_table.create(engine)

##composite keys can be used when you want to layer catagories in a table. for example, in an items table weapons could have an item_id of 1 and each distinct weapon would then have a numeric id, unique within the weapon subcatagory but by itself not unique in the item table

    #ForeignKeyConstraint(
    #                ["local_column_name1", "local_colum_name2"],
    #                ["foreign_table.foreign_column_name1", foreign_table.foreign_column_name2]
    #)

###########################################
#Reflection - copying a table to a different metadata instance
###########################################

metadata2 = MetaData()
user_reflected = Table('user', metadata2, autoload=True, autoload_with=engine)

###########################################
#Inspector
###########################################

from sqlalchemy import inspect

inspector = inspect(engine)
inspector.get_table_names()
#[addresses, fancy, network, ...]

inspector.get_columns('address')
#returns detailed dictionary with column info

inspector.get_foreign_keys()

###########################################
#Basic Data Types
###########################################
'''
integer
string
unicode
boolean
datetime
float
numeric(x, y)
'''

###########################################
#Create and Drop methods
###########################################

#metadata.create_all(engine, checkfirst=True)
#table.create(engine, checkfirst=False)
#metadata.drop_all(engine, checkfirst=True)
#table.drop(engine, checkfirst=False)

###########################################
#basic sql operators
###########################################

#| or or_
#and_
#== or is_

from sqlalchemy import and_, or_

print(
    and_(
        user_table.c.fullname == 'ed jones',
            or_(
                user_table.c.username == 'ed',
                user_table.c.username == 'jack'
            )
        )
    )
#"user".fullname = :fullname_1 AND ("user".username = :username_1 OR "user".username = :username_2)

print(user_table.c.id > 5)
#"user".id > :id_1

print(user_table.c.fullname == None)
#"user".fullname IS NULL

print(user_table.c.fullname.is_(None))
#"user".fullname IS NULL

print(user_table.c.id + 5)
#"user".id + :id_1

print(user_table.c.fullname + "some name")
#"user".fullname || :fullname_1