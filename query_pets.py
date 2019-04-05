# sudo apt-get install python-mysqldb

import MySQLdb

person_id = input("Enter person id number")

db = MySQLdb.connect(host="localhost",
					 user="root",
                     passwd="axat",
                     db="person")  

cur = db.cursor()
cur1 = cur.execute("SELECT * FROM person WHERE person_id = %s", str(person_id))
if cur1:
	for row in cur.fetchall():
		"James Smith owned Rusty, a dalmatian, that was 4 years old"
		print (row[1]+" "+row[2]+", "+str(row[3])+" years old")
else:
	print ("person data not available")

cur = db.cursor()

aaa = "SELECT * FROM person p INNER JOIN person_pet ps ON p.person_id="+str(person_id)+" INNER JOIN pet pe ON pe.pet_id=ps.pet_id WHERE ps.person_id="+str(person_id)+" AND ps.pet_id="+str(person_id)

cur.execute(aaa)

if cur.fetchall():
	for row in cur:
		print (str(row[1])+" "+str(row[2])+" owned "+str(row[7])+", a "+str(row[8])+", that was "+str(row[9])+ " years old")
else:
	print ("person_pets table data not available")