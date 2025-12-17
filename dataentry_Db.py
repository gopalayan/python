import mysql.connector
dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="W2002@gopal#",
    database="mckv"
)
createobj=dataBase.cursor()
sql="INSERT INTO STUDENT(NAME,BRANCH,ROLL) VALUES(%s,%s,%s)"
val=("gopal","aiml","32")
createobj.execute(sql,val)
dataBase.commit()
dataBase.close()