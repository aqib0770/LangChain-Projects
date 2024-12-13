import sqlite3
connection = sqlite3.connect("Student.db")
cursor = connection.cursor()
table_info = """
create table STUDENT(NAME VARCHAR(15), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

cursor.execute('''Insert Into Student values('Krish', 'Data Science', 'A', 90);''')
cursor.execute('''Insert Into Student values('Aqib', 'Computer Science', 'B', 100);''')
cursor.execute('''Insert Into Student values('Riyan', 'Information Technology', 'C', 70);''')
cursor.execute('''Insert Into Student values('Salahuddin', 'Information Technology', 'A', 75);''')
cursor.execute('''Insert Into Student values('Ibrahim', 'Photography', 'C', 110);''')

print("The inserted records are")
data = cursor.execute('''Select * from Student;''')
for row in data:
    print(row)

connection.commit()
connection.close()
