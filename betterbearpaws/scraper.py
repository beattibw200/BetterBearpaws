
# Scraper.py scans pdf of Potsdam Course List and scans each line to pull out
# lines that contain course data. Then the line is cut into each piece of Course
# info and creates a Course object.


# importing required modules
import PyPDF2
import re
import io
from Course import Course

# creating a pdf file object
pdfFileObj = open('filetoscrape.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(0)
# extracting lines from pdf
words = pageObj.extractText()

# Seperating line into groups that hold each piece of course information.
line_re = re.compile(r'(\d{5}) (\w{2,4})\s*(\d{3})  (.*?)  (.*?) \s*(\d)(.*M{1})(.*?[\dA{1}])\s{1,2}(\w\s\w*) \s*(\d*)\s*(\d*) \s*\d*\w*\s*(.*)')

# For loop goes through each line of pdf and saves each group into variables.
for line in io.StringIO(words):

    newCourse = line_re.match(line)
    # Checks if line contains course data.
    if newCourse:
        # Sets appropriate groups equal to matching variables.
        CRN = newCourse.group(1)
        department = newCourse.group(2)
        section = newCourse.group(4)
        title = newCourse.group(5)
        credits = newCourse.group(6)
        enrolled = newCourse.group(9)
        max = newCourse.group(8)
        if not (newCourse.group(12).isupper()):
            genEd = "none"
        else:
            genEd = newCourse.group(12)

        # Creates id for course.
        id = department + " " + newCourse.group(3)
        # Creates course with course id
        id = Course(CRN,department,section,title,credits,enrolled,max,genEd)

        #print(id.title)

# closing the pdf file object
pdfFileObj.close()
