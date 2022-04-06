import pytest
from connection import connection
from demo import all
# tests will be here

#can I connect to the database?
def test_createConnection(dsn):
    conn = connection.connect(dsn)
    assert not conn.closed
    assert conn.pgconn.status == conn.ConnStatus.OK
    conn.close()

# async def test_createConnection(dsn):
#     conn = await AsyncConnection.connect(dsn)
#     assert not conn.closed
#     assert conn.pgconn.status == conn.ConnStatus.OK
#     await conn.close()