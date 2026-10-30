import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Nithyamradhe@12",database="employees")
cursor=connection.cursor()
cursor.execute('select * from employees limit 3')
result=cursor.fetchall()
print(result)