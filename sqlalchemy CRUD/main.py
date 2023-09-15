from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///sample.db", echo=True)
print("ENGINE", engine)
print("TYPE OF ENGINE", type(engine))

meta= MetaData()

# There are 2 ways to create tables 
# 1. using declarative_base class 
# 2. Table class 
workers = Table(
    'workers',
    meta,
    Column('id', Integer,primary_key = True),
    Column('name', String)
)


# Below line is used to create the table in the database 
# Once the database and table is created we donot need this line so I have commented it out 
# meta.create_all(engine)


# Inserting into Database
ins = workers.insert().values(name="Mana")
print("INSTANCE TO INSERT: ", ins)
print("Type OF INSTANCE TO INSERT: ", type(ins))

conn = engine.connect()
print("CONNECTION: ", conn)
result = conn.execute(ins)
print("RESULT: ", result)
print("TYPE OF RESULT: ", result)