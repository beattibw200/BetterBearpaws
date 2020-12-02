from pymongo import MongoClient
client = MongoClient()

db = client.Project

#Takes: List of Course objects
#Converts each Course into a MongoDB document
#and inserts into Courses collection in database
#Prints: Success and resulting Object ID from MongoDB
def insert_courses(courses_obj):

    Courses = db.Courses

    for x in courses_obj:
        course_data = {
            "crn": x.CRN,
            "title": x.title,
            "sect": x.section,
            "dept": x.department,
            "credits": x.credits,
            "capactiy": x.max,
            "enrolled": x.enrolled
            }

        result = courses.insert_one(course_data)
        print('One course: {0}'.format(result.inserted_id))

