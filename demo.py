# This is where you'll execute a series of SQL statements during demo day.
#from connection import connection
from connection import execute_query


create_table = """
    DROP TABLE citizens;
    CREATE TABLE citizens (
        name varchar,
        id int GENERATED ALWAYS AS IDENTITY,
        alive varchar);
    """

execute_query(create_table)

# delete_table = """
#     DROP TABLE citizens
# """

# execute_query(delete_table)

# for hero in heroes:
#     print(hero)
# 
# # select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """