import mysql.connector

# connect database
myDb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#iqbal99",
    database="mydatabase"
)

myCursor = myDb.cursor()

# insert value

insert_sql_command = """
                        INSERT INTO Student(roll, first_name, last_name)
                        VALUES(1, "Iqbal", "Hossan")
                     """

myCursor.execute(insert_sql_command)

# it have to use to insert data in database
myDb.commit()