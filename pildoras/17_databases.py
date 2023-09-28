"""
Class 55: Databases part 1: create and connect with db
Class 56: Databases part 2: insert several records and retrieve data
Class 57: Databases part 3: create tables with unique ids
Class 58: Databases part 4: CRUD
Author: Eliana Chavez
"""

# 1. Create or open connection
# 2. Create cursor
# 3. Execute query
# 4. Manage results
# 5. Close cursor and connection

# Library that creates embbebed database and allows us to interact with it
import sqlite3


def connect(databaseName):
    connection = sqlite3.connect(databaseName)
    return connection


def executeQuery(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def executeManyQueries(connection, query, params):
    cursor = connection.cursor()
    cursor.executemany(query, params)
    connection.commit()


def closeConnection(connection):
    connection.close()


def createDbAndFirstRecordExample():
    connection = connect("test")
    query = "CREATE TABLE PRODUCTS (NAME VARCHAR(50), PRICE INTEGER, SECTION VARCHAR(20))"
    query2 = "INSERT INTO PRODUCTS VALUES('WATCH',10000,'TECH')"
    executeQuery(connection, query)
    executeQuery(connection, query2)
    closeConnection(connection)


def insertSeveralRecordsExample():

    products = [
        ("PHONE", 1500, "TECH"),
        ("SHIRT", 300, "CLOTHS"),
        ("MOUSE", 150, "TECH"),
    ]

    connection = connect("test")
    query = "INSERT INTO PRODUCTS VALUES(?,?,?)"
    executeManyQueries(connection, query, products)
    closeConnection(connection)


def retrieveDataExample():
    connection = connect("test")
    query = "SELECT * FROM PRODUCTS"
    cursor = connection.cursor()
    cursor.execute(query)
    # return cursor.fetchall()
    products = cursor.fetchall()

    for p in products:
        print("Name: ", p[0], "\nPrice: ", p[1], "\nSection: ", p[2])


def createTableWithIndexExample():
    connection = connect("test")
    query = """
    CREATE TABLE PRODUCTS2 (
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      NAME VARCHAR(50), 
      PRICE INTEGER, 
      SECTION VARCHAR(20))
    """
    # For auto increment ids it should be specified with null
    query2 = "INSERT INTO PRODUCTS2 VALUES(NULL,?,?,?)"

    products = [
        ("PHONE", 1500, "TECH"),
        ("SHIRT", 300, "CLOTHS"),
        ("MOUSE", 150, "TECH"),
    ]
    executeQuery(connection, query)
    executeManyQueries(connection, query2, products)
    closeConnection(connection)


def updateRecordExample():
    connection = connect("test")
    # For auto increment ids it should be specified with null
    query = "UPDATE PRODUCTS2 SET NAME = 'TV' WHERE ID = 1"

    executeQuery(connection, query)

    closeConnection(connection)


def deleteRecordExample():
    connection = connect("test")
    # For auto increment ids it should be specified with null
    query = "DELETE FROM PRODUCTS2 WHERE ID = 2"

    executeQuery(connection, query)

    closeConnection(connection)

# Data in database can be visualized using DB Browser for SQLite opening the db file


def main():
    # createDbAndFirstRecordExample()
    # insertSeveralRecordsExample()
    # print(retrieveDataExample())
    # createTableWithIndexExample()
    updateRecordExample()
    deleteRecordExample()


main()
