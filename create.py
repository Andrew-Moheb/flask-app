import sqlite3  

connection = sqlite3.connect("users_data.db")    


cursor = connection.cursor() 

cursor.execute("INSERT INTO users VALUES ('andrew','0000')") 

cursor.execute("INSERT INTO users VALUES ('maged','1111')")

cursor.execute("INSERT INTO users VALUES ('omar','2222')")  

connection.commit()







