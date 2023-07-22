import mysql.connector

# connect mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#iqbal99",
    database="mydatabase"
)

myCursor = mydb.cursor()

select_sql_command = """
                        SELECT *
                        FROM Student
                      """

myCursor.execute(select_sql_command)

# use fetchall to get all data from database table
data = myCursor.fetchall()

for i in data:
    print(i)