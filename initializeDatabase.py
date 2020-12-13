# initializeDatabase.py initializes the BetterBearPaws database
# (currently only builds Courses table)
# Connects to MongoDB on local connection and creates BetterBearPaws database.
# Uses scraper.py to scrape Potsdam Course List for course info.
# Then it uses insert_courses(list, dict) to fill the Courses collection (table)
import scraper
import inserts

from pymongo import MongoClient

#Initializes database
client = MongoClient()
db = client['BetterBearPaws']

#Executes scraper.py to get course_list
print("Running scraper.py...")
execfile('scraper.py')

#Get the list to send to insertCourses
course_list = scraper.getList()

#Run insert_courses from inserts to insert the courses
#into the MongoDB
print("Running inserts.insert_courses...")
inserts.insert_courses(course_list, db)

print("Done!")

print("Running inserts.insert_profs...")
inserts.insert_profs(scraper.getProfs(), db)

print("Done!")

print("Running inserts.insert_teaches...")
inserts.insert_teaches(course_list, db)

print("Done!")
