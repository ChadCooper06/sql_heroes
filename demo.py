# This is where you'll execute a series of SQL statements during demo day.
#from connection import connection
import psycopg
from connection import create_connection
from connection import execute_query

#---INPUT FROM USER---
def startup():
    prompt = input("Select an option\n A- Look up a hero\n B- Add your secret identity\n C- Change your info\n D- Delete your info\n")
    choice = prompt
    if choice == 'A' or 'a':
        print("Who do you want to look up?\n")
        hero = input()
        search_hero(hero) # look up the info for a specific hero
    elif choice == 'B' or 'b':
        print("What is your secret identity?\n")
        hero_name = input()
        print("What is your power?\n")
        hero_power = input()
        print("Tell us a little about you.\n")
        hero_bio = input()
        create_hero(hero_name, hero_power, hero_bio)# create a new hero with those inputs
    elif choice == 'C' or 'c':
        option = input("Would you like to change your info? Select N for name\n S for power-Please list all\n or I for biography.\n")
        correction = option
        if correction == 'N' or 'n':
            print("Changing your name huh? Who are you?\n")
            name = input()
            print("Go ahead, confuse everyone.\n")
            new_name = input()
            name_change(new_name)# change the name of the individual hero
        elif correction == 'S' or 's':
            print("Did you fall into more toxic goo? What's your name?\n")
            name = input()
            print("Remember to add all your powers.\n")
            new_about = input()
            change_power(new_about)# change the power(s) of the individual hero
        elif correction == 'I' or 'i':
            print("Having an identity crisis? Who hurt you? Type your name.\n")
            name = input()
            print("Type the info no one will read EXCEPT that ONE guy, you now who I mean. The creepy one...Jeff.\n")
            new_bio = input()
            change_bio(new_bio)# change the bio of the individual hero
    elif choice == 'D' or 'd':
        print("Are you deleting to go into hiding or because you killed the person? Know what, nevermind that. Please type the name to be deleted.\n")
        name = input()
        delete_hero(name)# delete a hero
    elif choice == 'X' or 'x':
        statement = input("Oh you\'re a clever one huh? Fine, want to see every hero?\n Y or N\n")
        pick = statement
        if pick == 'Y' or 'y':
            print("Please don\'t do anything nefarious with this information...wink, wink.\n")
            show_heroes()# show all heroes and info
        elif pick == 'N' or 'n':
            print("Knew you were lame.")
            startup()
startup()

#######################
# FUNCTIONS FOR DOING #
#######################
#--- SEARCH HERO INFO ---

def search_hero(name):
    search_hero = """
        SELECT * FROM heroes
        WHERE name = '{}';
    """.format(name)
    execute_query(search_hero)
print("That\'s all that is known.")

#--- CREATE A HERO ---

def create_hero(hero_name, hero_power, hero_bio):
    create_hero = """
        INSERT INTO heroes(name, about_me, biography)
        VALUES ('{}', '{}', '{}');
        """.format(hero_name, hero_power, hero_bio)
    execute_query(create_hero)
print("The city just got a little safer.")


#--- CHANGE NAME ---

def name_change(new_name, name):
    name_change = """
        UPDATE heroes
        SET name = '{}'
        WHERE name = '{}';
    """.format(new_name, name)
    execute_query(name_change)
print("Name change successful!")

#--- CHANGE A POWER ---

def change_power(new_about, name):
    change_power = """
        UPDATE heroes
        SET about_me = '{}'
        WHERE name = '{}';
        """.format(new_about, name)
    execute_query(change_power)
print("Powers updated!")
    
#--- CHANGE BIO ---

def change_bio(new_bio, name):
    change_bio = """
        UPDATE heroes
        SET biography = '{}'
        WHERE name = '{}';
        """.format(new_bio, name)
    execute_query(change_bio)
print("Bio updated!")

#--- DELETE SOMEONE ---

def delete_hero(name):
    delete_hero = """
        DROP *
        FROM heroes
        WHERE name = '{}';
    """.format(name)
    execute_query(delete_hero)
print("So sad....")

#--- SHOW ALL ---

def show_heroes():
    show_heroes = """
        SELECT * FROM heroes
        ORDER BY name ASC; 
    """
print(execute_query(show_heroes))

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