# import psycopg
# import sys
# sys.path.append('/workspace/sql_heroes/')
# from connection import create_connection, execute_query
# import demo

# #######################
# # FUNCTIONS FOR DOING #
# #######################

# #--- SEARCH HERO INFO ---#

# def search_hero(name):
#     execute_query("""
#         SELECT * FROM heroes
#         WHERE name = %s;
#     """, [name])
#     print("That\'s all that is known.")

# #--- CREATE A HERO ---$

# def create_hero(hero_name, hero_power, hero_bio):
#     execute_query("""
#         INSERT INTO heroes(name, about_me, biography)
#         VALUES (%(name)s, %(about_me)s, %(biography)s);
#         """, {'name': "hero_name", 'about_me': "hero_power", 'biography': "hero_bio"})
#     print("The city just got a little safer.")

# #--- CHANGE NAME ---#

# def name_change(new_name, name):
#     execute_query("""
#         UPDATE heroes
#         SET name = %(new_name)s
#         WHERE name = %(name)s;
#     """, {'new_name': "new_name", 'name': "name"})
#     print("Name change successful!")

# #--- CHANGE A POWER ---#

# def change_power(new_about, name):
#     execute_query("""
#         UPDATE heroes
#         SET about_me = %(new_about)s
#         WHERE name = %(name)s;
#         """, {'new_about': "new_about", 'name': "name"})
#     print("Powers updated!")
    
# #--- CHANGE BIO ---#

# def change_bio(new_bio, name):
#     execute_query("""
#         UPDATE heroes
#         SET biography = %(new_bio)s
#         WHERE name = %(name)s;
#         """, {'new_bio': "new_bio", 'name': "name"})
#     print("Bio updated!")

# #--- DELETE SOMEONE ---#

# def delete_hero(name):
#     execute_query("""
#         DELETE
#         FROM heroes
#         WHERE name = %s;
#     """, [name])
#     print("So sad....")

# #--- SHOW ALL ---#

# def show_heroes(params):
#     execute_query("""
#         SELECT * FROM heroes
#         ORDER BY name ASC; 
#     """, params)
#     print(show_heroes)