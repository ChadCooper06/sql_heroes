# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query

select_heroes = """
    SELECT * FROM heroes
    ORDER BY id DESC 
"""

heroes = execute_query(select_heroes).fetchall()
for hero in heroes:
    print(hero[1])