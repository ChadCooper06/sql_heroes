
def create_hero():
    """
    DELETE FROM heroes
    WHERE name = 'C0de M4n';

    INSERT INTO heroes(name, about_me, biography)
    VALUES ('C0de M4n', 'Breaks the internet.', 'Did you try turning it off then back on?');
    """
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return cursor
    except OperationalError as e:
        print("The error '{e}' occurred")


#---SETTING UP A REQUEST FOR INFORMATION ABOUT 1 HERO---
def lookup_hero(name, about_me):
    lookup = """
    SELECT name, about_me
    FROM heroes
    WHERE name = '{}'
    """.format(name)
    execute_query(lookup)

#---SETTING UP REQUEST FOR WHO A HERO IS FRIENDS WITH---
def hero_friends(hero1_id, hero2_id, relationship_type_id):
    friends = """
    SELECT hero2_id
    FROM relationships
    WHERE hero1_id = 3 AND relationship_type_id = 1;
    """.format()
    execute_query(friends)


# sql1 = '''SELECT * {0}
# FROM {1} INNER JOIN {2}
# ON {1}.{3} = {2}.{3}
# Order By {4} desc;
# '''

# print(sql1.format('Spot','Dogs', 'Owners', 'DogID', 'Speed'))


#---MORE ADVANCED---
def friend_names():
    #nested query where the outer displays the result of the inner
    super_friends = """
    SELECT name
    FROM heroes
    WHERE id IN (
		SELECT hero2_id
		FROM relationships
		WHERE hero1_id = 3 AND relationship_type_id = 1);
    """
    print('McMuscles is friends with {name}, {name}, and {name}.')