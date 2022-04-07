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
        print("Who do you want to look up?")
        hero = input()
        search_hero(hero)# look up the hero info
    elif choice == 'B' or 'b':
        print("What is your secret identity?")
        hero_name = input()
        print("What is your power?")
        hero_power = input()
        print("Tell us a little about you.")
        hero_bio = input()
        create_hero(hero_name, hero_power, hero_bio)# create a new hero with those inputs
    elif choice == 'C' or 'c':
        option = input("Would you like to change your info? Select N for name\n S for power-Please list all\n or I for biography.")
        correction = option
        if correction == 'N' or 'n':
            print("Changing your name huh? Who are you?")
            name = input()
            print("Go ahead, confuse everyone.")
            new_name = input()
            name_change(new_name)
        elif correction == 'S' or 's':
            print("Did you fall into more toxic goo? What's your name?")
            name = input()
            print("Remember to add all your powers")
            new_about = input()
            change_power(new_about)
        elif correction == 'I' or 'i':
            print("Having an identity crisis? Who hurt you? Type your name.")
            name = input()
            print("Type the info no one will read EXCEPT that ONE guy, you now who I mean. The creepy one.")
            new_bio = input()
            change_bio(new_bio)

    #print(f"New hero {name} with power of {power} and bio of {bio} added to the registry")

#---CREATE A HERO---

def create_hero(hero_name, hero_power, hero_bio):
    create_hero = """
        INSERT INTO heroes(name, about_me, biography)
        VALUES ('{hero_name}', '{hero_power}', '{hero_bio}');
        """
    (execute_query(create_hero))

    #print('New Hero found!')

#---CHANGE NAME---

def name_change(new_name):
    name_change = """
        UPDATE heroes
        SET name = '{new_name}'
        WHERE name = '{name}';
    """
    execute_query(name_change)
    # for n in new_name:
    #     print("Who are you "+n[0]+"?")

#---CHANGE A POWER---

def change_power(new_about, name):
    change_power = """
        UPDATE heroes
        SET about_me = '{new_about}'
        WHERE name = '{name}';
        """
    execute_query(change_power)
    # for p in powers:
    #     print("New powers are "+p[0]+"!")

#---CHANGE BIO---

def change_bio(new_bio, name):
    change_bio = """
        UPDATE heroes
        SET biography = '{new_bio}'
        WHERE name = '{name}';
        """
    execute_query(change_bio)

#--------------

# def create_citizen():
#     avg_joe = """
#     INSERT INTO citizens(name, alive)
    #   VALUES 
    #   ('Karen', 'Alive and kicking...and you will know it too'),
    #   ('Napolean', 'Alive and probably eating a burrito'),
    #   ('Jimothy', 'Dead...or is he?');
#     """.format()
#     print(execute_query(create_citizen))

 	

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