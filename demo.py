# This is where you'll execute a series of SQL statements during demo day.
#from connection import connection
import psycopg
from connection import connection
from connection import execute_query

# select_heroe = """
# SELECT * from heroes;
# """
# execute_query(select_heroes)

# create_table = """
# DROP TABLE citizens;
# CREATE TABLE citizens (
#     name varchar,
#     id int GENERATED ALWAYS AS IDENTITY,
#     alive varchar);
# """

# execute_query(create_table)

# delete_table = """
#     DROP TABLE citizens
# """

# execute_query(delete_table)



# select_heroes = """
#     SELECT * FROM public.heroes:
#     ORDER BY id ASC; 
# """
# print(heroes)

# create_table = """
# CREATE TABLE accounts (
# 	user_id serial PRIMARY KEY,
# 	username VARCHAR ( 50 ) UNIQUE NOT NULL,
# 	password VARCHAR ( 50 ) NOT NULL,
# 	email VARCHAR ( 255 ) UNIQUE NOT NULL,
# 	created_on TIMESTAMP NOT NULL,
#     last_login TIMESTAMP 
# );
# """
# execute_query(create_table)

# delete_table = """
# DROP TABLE accounts;
# """
# execute_query(delete_table)

show_heroes = """
SELECT * FROM heroes;
"""
execute_query(show_heroes).fetchall()
print()