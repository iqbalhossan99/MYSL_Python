import mysql.connector

# connect mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#iqbal99"
)

# create a database
myCursor = mydb.cursor()

db_name = "mydatabase"
sql_command = "CREATE DATABASE " + db_name

myCursor.execute(sql_command)




