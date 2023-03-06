import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(123, 'sudh', 94.56, 101, 'Data Science')")
mydb.commit()
mydb.close()