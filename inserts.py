#Takes: List of Course objects
#Converts each Course into a MongoDB document
#and inserts into Courses collection in database

def insert_courses(courses_obj, c):

    #initalize Courses table


    #iterate over array of Course objects and
    #insert each Course as a document (tuple)

    courses_data = []
    
    for x in courses_obj:
        course_data = (
            x.ID,
            x.CRN,
            x.title,
            x.section,
            x.department,
            x.credits,
            x.max,
            x.enrolled
            )

        courses_data.append(course_data)

    c.executemany('INSERT INTO Courses VALUES (?,?,?,?,?,?,?,?)', courses_data)

def insert_profs(profs_set, c):
    profs = []
    for x in profs_set:
        profs.append((x,))

    c.executemany('INSERT INTO Professors VALUES (?)', profs)

def insert_teaches(courses_obj, c):
    

    teaches = []

    for x in courses_obj:
        teach_data = (
            x.prof,
            x.CRN
        )
        teaches.append(teach_data)
    c.executemany('INSERT INTO teaches VALUES (?,?)', teaches)

def insert_students(c):

    print("Running inserts.insert_students...")
    print("Running webscrape.py...")
    print("(This one could take a while)")
    import webscrape
    stu_list = webscrape.getStudents()
    for x in stu_list:
        stu_data = (
            x.pnum,
            x.name
        )
        c.execute('INSERT INTO Students VALUES (?,?)', stu_data)
        stu_takes = []
        stu_needs = []
        for y in x.takes:
            stu_takes.append((x.pnum, y))
        for y in x.need:
            stu_needs.append((x.pnum, y))           
        c.executemany('INSERT INTO needs VALUES (?,?)', stu_needs)
        c.executemany('INSERT INTO has_taken VALUES (?,?)', stu_takes)


