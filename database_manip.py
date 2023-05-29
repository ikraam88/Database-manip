import sqlite3
# make connection to database
db = sqlite3.connect('data/student_db')
# create cursor object
cursor = db.cursor()
# create table called "python_programming"
cursor.execute('''CREATE TABLE python_programming
                (id INTEGER PRIMARY KEY,
                 name TEXT,
                 grade INTEGER)''')
# insert data as rows in the table
cursor.execute("INSERT INTO python_programming VALUES (55, 'Carl Davis', 61)")
cursor.execute("INSERT INTO python_programming VALUES (66, 'Dennis Fredrickson', 88)")
cursor.execute("INSERT INTO python_programming VALUES (77, 'Jane Richards', 78)")
cursor.execute("INSERT INTO python_programming VALUES (12, 'Peyton Sawyer', 45)")
cursor.execute("INSERT INTO python_programming VALUES (2, 'Lucas Brooke', 99)")

# commit changes
db.commit()

# Select all records of grades between 60 and 80
cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
print(cursor.fetchall())
print("All records with grade of 60 to 80!")

# Change grade => 65
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")
print("Carl Davis' grade changed to 65!")

# Delete Dennis' row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")
print("Dennis Frederickison's row deleted!")

# Change grade of all with id < 55
cursor.execute("UPDATE python_programming SET grade = 45 WHERE id < 55")
print("All people with an id<55 grade changed to 45!")
# Commit the changes to the database
# Close the connection
db.commit()
db.close()
print('Connection to database closed')
