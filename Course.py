# Course object created to hold information about a course.

## Added prof to construct teaches table with

class Course:
    def __init__(self, CRN, department, section, title, credits, enrolled, max, genEd, prof):
        self.CRN = CRN
        self.department = department
        self.section = section
        self.title = title
        self.credits = credits
        self.enrolled = enrolled
        self.max = max
        self.genEd = genEd
        self.prof = prof
