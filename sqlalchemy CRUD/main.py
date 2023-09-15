from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///sample.db", echo=True)
print(engine)
print(type(engine))

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

meta.create_all(engine)
