import mysql.connector

# connect database
myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#iqbal99",
    database="mydatabase"
)

myCursor = myDb.cursor()

# create table
sql_command = """
                CREATE TABLE Student(
                    roll INT,
                    first_name VARCHAR(20),
                    last_name VARCHAR(20)
                )

"""

myCursor.execute(sql_command)
