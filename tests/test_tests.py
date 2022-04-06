# import pytest
# from connection import create_connection
# from demo import all
# # tests will be here

# #can I connect to the database?
# def test_createConnection(dsn):
#     conn = connection.connect(dsn)
#     assert not conn.closed
#     assert conn.pgconn.status == conn.ConnStatus.OK
#     conn.close()

# def test_hero():
#     heroes = execute_query