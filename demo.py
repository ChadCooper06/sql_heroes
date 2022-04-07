# This is where you'll execute a series of SQL statements during demo day.
#from connection import connection
import psycopg
from connection import create_connection
from connection import execute_query

#---INPUT FROM USER---
def startup():
    prompt = input("Select an option\n A- Look up a hero\n B- Add your secret identity\n C- Change your info\n D- Delete your info")
    choice = prompt
    if choice == 'A' or 'a':

        "name: \n"
        "power: \n"
        "bio: "
    print(f"New hero {name} with power of {power} and bio of {bio} added to the registry")

#---CREATE A HERO---

def create_hero():
    create_hero = """
        INSERT INTO heroes(name, about_me, biography)
        VALUES ('MisleToe', 'I never miss!', 'A fungal infection caused his toes to literally become missiles...no, LITERALLY!');
        """
    print(execute_query(create_hero))

    #print('New Hero found!')

#---CHANGE NAME---

def name_change():
    name_change = """
        UPDATE heroes
        SET name = 'MissileToe'
        WHERE id = 39;
    """
    new_name = (execute_query(name_change))
    for n in new_name:
        print("Who are you "+n[0]+"?")

#---CHANGE A POWER(OR ANYTHING)---

def change_power():
    change_power = """
        UPDATE heroes
        SET about_me = 'Creates code and smart remarks'
        WHERE name = 'C0de M4n';
        """
    powers = (execute_query(change_power))
    for p in powers:
        print("New powers are "+p[0]+"!")

#--------------

# def create_citizen():
#     avg_joe = """
#     INSERT INTO citizens (name, alive)
#     VALUES ('Lewis', 'Just Barely')
#     """.format()
#     print(execute_query(create_citizen))

#  INSERT INTO citizens(name, alive)
#  VALUES 
#  	('Karen', 'Alive and kicking...and you will know it too'),
# 	('Napolean', 'Alive and probably eating a burrito'),
# 	('Jimothy', 'Dead...or is he?');
 	

#---FIND WHO IS FRIENDS WITH MCMUSCLES---

    #nested query where the outer displays the result of the inner
def friend_names():
    super_friends = """
    SELECT name
    FROM heroes
    WHERE id IN (
		SELECT hero2_id
		FROM relationships
		WHERE hero1_id = 3 AND relationship_type_id = 1);
    """
    friends = (execute_query(super_friends).fetchall())
    for x in friends:
        print("McMuscles is friends with " +x[0]+".")


#-----------

# delete_table = """
#     DROP TABLE citizens
# """

# execute_query(delete_table)



# select_heroes = """
#     SELECT * FROM public.heroes:
#     ORDER BY id ASC; 
# """
# print(heroes)



# select_heroes = """
# SELECT * from heroes;
# """
# execute_query(select_heroes).fetchone()
# print (The Seer)

# create_table = """
# CREATE TABLE citizens (
#     name varchar,
#     id int GENERATED ALWAYS AS IDENTITY,
#     alive varchar);
# """
# execute_query(create_table)