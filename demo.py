import psycopg
import sys
sys.path.append('/workspace/sql_heroes/.') #fixes the pathways being unable to communicate properly
from connection import create_connection, execute_query

#######################
# FUNCTIONS FOR DOING #
#######################

#--- SEARCH HERO INFO ---#

def search_hero(name): # The execute_query sends the SQL in it to the DB to make changes or calls depending on request
    hero = execute_query("""
        SELECT name, about_me 
        FROM heroes
        WHERE name = %s
    """, (name,)).fetchall()
    print("What we know is:\n")
    print(hero[0])

#--- CREATE A HERO ---#

def create_hero(hero_name, hero_power, hero_bio): # The %s is a string placeholder for the information to be used as variables
    execute_query("""
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s) 
        """, [hero_name, hero_power, hero_bio])
    print("Welcome hero! The city just got a little safer.")

#--- CHANGE NAME ---#

def name_change(name, new_name):
    execute_query("""
        UPDATE heroes
        SET name = %s
        WHERE name IN (
            SELECT name
            FROM heroes
            WHERE name = %s
        )
    """, (new_name, name))
    print("Name change successful!")

#--- CHANGE A POWER ---#

def change_power(name, about_me):
    execute_query("""
        UPDATE heroes
        SET about_me = %s
        WHERE name in (
            SELECT name
            FROM heroes
            WHERE name = %s)
        """, [about_me, name])
    print("Powers updated!")
    
#--- CHANGE BIO ---#

def change_bio(name, biography):
    execute_query("""
        UPDATE heroes
        SET biography = %s
        WHERE name IN (
            SELECT name
            FROM heroes
            WHERE name = %s
        )
        """, [biography, name])
    print("Bio updated!")

#--- DELETE SOMEONE ---#

def delete_hero(name):
    execute_query("""
        DELETE
        FROM heroes
        WHERE name = %s
    """, (name,))
    print("So sad....Would you like some cake?")

#--- SHOW ALL ---#

def show_heroes(): # This will print the info for every hero, but is only accessed if you know the right key to press
    heroes = execute_query("""
        SELECT name, about_me, biography
        FROM heroes
        ORDER BY name ASC;
    """).fetchall()
    for hero in heroes:
        print(hero)
        print("\n")

##################
# READY PLAYER 1 #
##################

#--- INPUT FROM USER ---#

def startup(): # Runs as soon as python loads this file-very much enjoyed making this-sorry for the snarky prompts :P
    prompt = input("\nSelect an option\n" 
        "A- Look up a hero\n" 
        "B- Add your secret identity\n" 
        "C- Change your info\n" 
        "D- Delete your info\n")
    choice = prompt.lower() # lowercases the letters
    if  choice == 'a':
        print("\nWho do you want to look up?\n")
        hero = input()
        search_hero(hero) # look up the info for a specific hero
        startup() # Recycles back to the initial prompt after each successful running of a function
    elif choice == 'b':
        print("\nWhat is your secret identity?\n")
        hero_name = input()
        print("What is your power?\n")
        hero_power = input()
        print("Tell us a little about you.\n")
        hero_bio = input()
        create_hero(hero_name, hero_power, hero_bio) # create a new hero with those inputs
        startup()
    elif choice == 'c':
        option = input("\nWould you like to change your info? Select\n" 
            "N for name\n"
            "S for power-Please list all\n" 
            "I for biography.\n")
        correction = option.lower()
        if correction == 'n':
            print("\nChanging your name huh? Who are you?\n")
            name = input()
            print("\nGo ahead, confuse everyone.\n")
            new_name = input()
            name_change(name, new_name) # change the name of the individual hero
        elif correction == 's':
            print("\nDid you fall into more toxic goo? What's your name?\n")
            name = input()
            print("\nRemember to add all your powers.\n")
            about_me = input()
            change_power(name, about_me) # change the power(s) of the individual hero
        elif correction == 'i':
            print("\nHaving an identity crisis? Who hurt you? Type your name.\n")
            name = input()
            print("\nType the info no one will read EXCEPT that ONE guy, you now who I mean. The creepy one...Jeff.\n")
            new_bio = input()
            change_bio(name, new_bio) # change the bio of the individual hero
            startup()
        else: print("\nSomething went wrong\n") # My catch all in case something is not input correctly
        startup()
    elif choice == 'd':
        print("\nAre you deleting to go into hiding or because you killed the person? Know what, nevermind that.\n" 
        "Please type the name to be deleted.\n")
        name = input()
        delete_hero(name) # delete a hero
        startup()
    elif choice == 'x':
        statement = input("\nOh you\'re a clever one huh? Fine, want to see every hero?\n Y or N\n")
        pick = statement.lower()
        if pick == 'y':
            print("\nPlease don\'t do anything nefarious with this information...wink, wink.\n")
            show_heroes() # show all heroes and info
            startup()
        elif pick == 'n':
            print("\nKnew you were lame.\n")
            startup()
        else: print("\nThey know...run!\n") # Another catch
    else: print("\nAH AH AH You didn\'t say the magic word!\n") # Defensive programming!
    startup()

startup() # restarts the whole program from the start


####################################################################
#-------------- OTHER FUNCTIONS TO INCORPORATE LATER --------------#

def create_citizen(params):
    execute_query("""
    INSERT INTO citizens(name, alive)
      VALUES 
      ('Clark Kent', 'Alive and kinda looks familiar.'),
      ('Citizen', 'Alive'),
      ('Danika', 'Alive');
    """,[params])
    print(create_citizen)


#---FIND WHO IS FRIENDS WITH MCMUSCLES---

    #nested query where the outer displays the result of the inner
def friend_names(params):
    super_friends = """
    SELECT name
    FROM heroes
    WHERE id IN (
		SELECT hero2_id
		FROM relationships
		WHERE hero1_id = 3 AND relationship_type_id = 1);
    """, [params]
    friends = (execute_query(super_friends, params).fetchall())
    for x in friends:
        print("McMuscles is friends with " +x[0]+".")

def not_friends(params):
    not_friends = """
    SELECT name 
    FROM heroes
    WHERE id IN (
        SELECT hero2_id
        FROM relationships
        WHERE hero1_id = 4 AND relationship_type_id = 2);
    """, [params]
    enemies = (execute_query(not_friends, params).fetchall())
    for x in enemies:
        print("Hummingbird is NOT friends with "+x[0]+".")