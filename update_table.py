import mysql.connector

# connect mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#iqbal99",
    database="mydatabase"
)

myCursor = mydb.cursor()

update_sql_command = """
                        UPDATE Student
                        SET first_name = "Novab"
                        WHERE roll = 2;
                      """

myCursor.execute(update_sql_command)
# it have to use to insert data in database
mydb.commit()