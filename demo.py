import psycopg
import sys
sys.path.append('/workspace/sql_heroes/.')
from connection import create_connection, execute_query

#######################
# FUNCTIONS FOR DOING #
#######################
#--- SEARCH HERO INFO ---

def search_hero(name):
    execute_query("""
        SELECT * FROM heroes
        WHERE name = %s;
    """, [name])
    print("That\'s all that is known.")

#--- CREATE A HERO ---

def create_hero(hero_name, hero_power, hero_bio):
    execute_query("""
        INSERT INTO heroes(name, about_me, biography)
        VALUES (%(name)s, %(about_me)s, %(biography)s);
        """, {'name': "hero_name", 'about_me': "hero_power", 'biography': "hero_bio"})
    print("The city just got a little safer.")

#--- CHANGE NAME ---

def name_change(new_name, name):
    execute_query("""
        UPDATE heroes
        SET name = %(new_name)s
        WHERE name = %(name)s;
    """, {'new_name': "new_name", 'name': "name"})
    print("Name change successful!")

#--- CHANGE A POWER ---

def change_power(new_about, name):
    execute_query("""
        UPDATE heroes
        SET about_me = %(new_about)s
        WHERE name = %(name)s;
        """, {'new_about': "new_about", 'name': "name"})
    print("Powers updated!")
    
#--- CHANGE BIO ---

def change_bio(new_bio, name):
    execute_query("""
        UPDATE heroes
        SET biography = %(new_bio)s
        WHERE name = %(name)s;
        """, {'new_bio': "new_bio", 'name': "name"})
    print("Bio updated!")

#--- DELETE SOMEONE ---

def delete_hero(name):
    execute_query("""
        DELETE
        FROM heroes
        WHERE name = %s;
    """, [name])
    print("So sad....")

#--- SHOW ALL ---

def show_heroes(params):
    execute_query("""
        SELECT * FROM heroes
        ORDER BY name ASC; 
    """, params)
    print(show_heroes)

def restart(startup):
    return startup()

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
# def friend_names():
#     super_friends = """
#     SELECT name
#     FROM heroes
#     WHERE id IN (
# 		SELECT hero2_id
# 		FROM relationships
# 		WHERE hero1_id = 3 AND relationship_type_id = 1);
#     """
#     friends = (execute_query(super_friends).fetchall())
#     for x in friends:
#         print("McMuscles is friends with " +x[0]+".")
