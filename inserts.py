#Takes: List of Course objects
#Converts each Course into a MongoDB document
#and inserts into Courses collection in database

def insert_courses(courses_obj, db):

    #initalize Courses collection (table)
    collection = db['Courses']

    #iterate over array of Course objects and
    #insert each Course as a document (tuple)
    for x in courses_obj:
        course_data = {
            "ID": x.ID,
            "crn": x.CRN,
            "title": x.title,
            "sect": x.section,
            "dept": x.department,
            "credits": x.credits,
            "capactiy": x.max,
            "enrolled": x.enrolled
            }

        result = collection.insert_one(course_data)
        print('One course: {0}'.format(result.inserted_id))

def insert_profs(profs_set, db):
    collection = db['Professors']

    for x in profs_set:
        prof_data = {
            "Name": x,
            "teaches": []
            }
        result = collection.insert_one(prof_data)
        print('One prof: {0}'.format(result.inserted_id))

def insert_teaches(courses_obj, db):
    collection = db['Professors']
    
    for x in courses_obj:
       result =  collection.update_one(
           {"Name": x.prof},
           {"$addToSet": { "teaches": x.ID}}, upsert = True
       )