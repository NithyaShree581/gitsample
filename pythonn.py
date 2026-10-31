import mysql.connector
from dotenv import load_dotenv
import os 
load_dotenv()
hostt=os.getenv("host")
userr=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")
connection=mysql.connector.connect(host="hostt",user="userr",password="password",database="database")
cursor=connection.cursor()
cursor.execute('select * from employees limit 3')
result=cursor.fetchall()
print(result)