# import psycopg
# import sys
# sys.path.append('/workspace/sql_heroes/')
# from connection import create_connection, execute_query
# import demo


# def startup():
#     prompt = input("Select an option\n A- Look up a hero\n B- Add your secret identity\n C- Change your info\n D- Delete your info\n")
#     choice = prompt
#     if choice == 'A' or 'a':
#         print("Who do you want to look up?\n")
#         hero = input()
#         search_hero(hero) # look up the info for a specific hero
#     elif choice == 'B' or 'b':
#         print("What is your secret identity?\n")
#         hero_name = input()
#         print("What is your power?\n")
#         hero_power = input()
#         print("Tell us a little about you.\n")
#         hero_bio = input()
#         create_hero(hero_name, hero_power, hero_bio)# create a new hero with those inputs
#     elif choice == 'C' or 'c':
#         option = input("Would you like to change your info? Select N for name\n S for power-Please list all\n or I for biography.\n")
#         correction = option
#         if correction == 'N' or 'n':
#             print("Changing your name huh? Who are you?\n")
#             name = input()
#             print("Go ahead, confuse everyone.\n")
#             new_name = input()
#             name_change(new_name)# change the name of the individual hero
#         elif correction == 'S' or 's':
#             print("Did you fall into more toxic goo? What's your name?\n")
#             name = input()
#             print("Remember to add all your powers.\n")
#             new_about = input()
#             change_power(new_about)# change the power(s) of the individual hero
#         elif correction == 'I' or 'i':
#             print("Having an identity crisis? Who hurt you? Type your name.\n")
#             name = input()
#             print("Type the info no one will read EXCEPT that ONE guy, you now who I mean. The creepy one...Jeff.\n")
#             new_bio = input()
#             change_bio(new_bio)# change the bio of the individual hero
#     elif choice == 'D' or 'd':
#         print("Are you deleting to go into hiding or because you killed the person? Know what, nevermind that. Please type the name to be deleted.\n")
#         name = input()
#         delete_hero(name)# delete a hero
#     elif choice == 'X' or 'x':
#         statement = input("Oh you\'re a clever one huh? Fine, want to see every hero?\n Y or N\n")
#         pick = statement
#         if pick == 'Y' or 'y':
#             print("Please don\'t do anything nefarious with this information...wink, wink.\n")
#             show_heroes()# show all heroes and info
#         elif pick == 'N' or 'n':
#             print("Knew you were lame.")
#             startup()
# startup()


#create_hero('Batman', 'Gadget user.', 'He is the dark knight...and super rich.')








# def create_hero():
#     """
#     DELETE FROM heroes
#     WHERE name = 'C0de M4n';

#     INSERT INTO heroes(name, about_me, biography)
#     VALUES ('C0de M4n', 'Breaks the internet.', 'Did you try turning it off then back on?');
#     """
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#         return cursor
#     except OperationalError as e:
#         print("The error '{e}' occurred")


# #---SETTING UP A REQUEST FOR INFORMATION ABOUT 1 HERO---
# def lookup_hero(name, about_me):
#     lookup = """
#     SELECT name, about_me
#     FROM heroes
#     WHERE name = '{}'
#     """.format(name)
#     execute_query(lookup)

# #---SETTING UP REQUEST FOR WHO A HERO IS FRIENDS WITH---
# def hero_friends(hero1_id, hero2_id, relationship_type_id):
#     friends = """
#     SELECT hero2_id
#     FROM relationships
#     WHERE hero1_id = 3 AND relationship_type_id = 1;
#     """.format()
#     execute_query(friends)


# # sql1 = '''SELECT * {0}
# # FROM {1} INNER JOIN {2}
# # ON {1}.{3} = {2}.{3}
# # Order By {4} desc;
# # '''

# # print(sql1.format('Spot','Dogs', 'Owners', 'DogID', 'Speed'))


# #---MORE ADVANCED---
# def friend_names():
#     #nested query where the outer displays the result of the inner
#     super_friends = """
#     SELECT name
#     FROM heroes
#     WHERE id IN (
# 		SELECT hero2_id
# 		FROM relationships
# 		WHERE hero1_id = 3 AND relationship_type_id = 1);
#     """
#     print('McMuscles is friends with {name}, {name}, and {name}.')