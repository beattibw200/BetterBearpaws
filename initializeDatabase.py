# initializeDatabase.py initializes the BetterBearPaws database
# (currently only builds Courses table)
# Connects to MongoDB on local connection and creates BetterBearPaws database.
# Uses scraper.py to scrape Potsdam Course List for course info.
# Then it uses insert_courses(list, dict) to fill the Courses collection (table)
import scraper
import inserts
import sqlite3


#Initializes database
conn = sqlite3.connect('BetterBearPaws.db')
c = conn.cursor()

c.execute('''CREATE TABLE Courses (ID text, CRN text, title text, sect text, dept text, credits int, capacity int, enrolled int) ''')
c.execute('''CREATE TABLE Professors (Name text)''')
c.execute('''CREATE TABLE teaches (ProfName text, CRN int)''')
c.execute('''CREATE TABLE Students (PNum text, Name text)''')
c.execute('''CREATE TABLE has_taken (PNum text, ID text)''')
c.execute('''CREATE TABLE needs (PNum text, ID text)''')


#Executes scraper.py to get course_list
print("Running scraper.py...")
exec(open("scraper.py").read())

#Get the list to send to insertCourses
course_list = scraper.getList()

#Run insert_courses from inserts to insert the courses
print("Running inserts.insert_courses...")
inserts.insert_courses(course_list, c)

print("Done!")

print("Running inserts.insert_profs...")
inserts.insert_profs(scraper.getProfs(), c)

print("Done!")

print("Running inserts.insert_teaches...")
inserts.insert_teaches(course_list, c)

print("Done!")

inserts.insert_students(c)


print("Done!")

conn.commit()

conn.close()

