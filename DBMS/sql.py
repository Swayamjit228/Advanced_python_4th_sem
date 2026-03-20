import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="04Jan2006@sjm",
    host="localhost",
    port=3306,
    database="giet"

)

cur = con.cursor()
# cur.execute("show databases")
# for x in cur:
#     print(x)
query = "select * from student"
query="select * FROM student where salary> 15000 and salary < 30000"
query="SELECT * FROM student where address != 'delhi'"
query="SELECT * FROM student WHERE desig != 'teacher'"
query="SELECT * FROM student WHERE name IN ('aman','naman')"
query="SELECT * FROM student WHERE name LIKE '%a%a%'"
query="SELECT * FROM student WHERE LENGTH(name)=5"
query="SELECT * FROM student WHERE address LIKE 'r%'"
query="SELECT * FROM student ORDER BY salary DESC LIMIT 3"
query="SELECT * FROM student WHERE salary=(SELECT MIN(salary) FROM student)"
query="SELECT SUM(salary) FROM student WHERE gender='male'"
query="SELECT AVG(salary) FROM student WHERE gender='female'"
query="SELECT COUNT(*) FROM student WHERE salary>20000"
query="SELECT desig,COUNT(*) FROM student GROUP BY desig"
query="SELECT gender,AVG(salary) FROM student GROUP BY gender"
query="SELECT address,SUM(salary) FROM student GROUP BY address"
query="SELECT desig,AVG(salary) FROM student GROUP BY desig HAVING AVG(salary)>20000"
query="SELECT address,COUNT(*) FROM student GROUP BY address HAVING COUNT(*)>1"
query="SELECT * FROM student WHERE salary>(SELECT AVG(salary) FROM student)"
query="SELECT * FROM student WHERE salary=(SELECT MAX(salary) FROM student)"
query="SELECT * FROM student WHERE salary=(SELECT MIN(salary) FROM student)"

cur.execute(query)

myresult = cur.fetchall()
for x in myresult:
    print(x)
    
# cur.close()
con.close()


