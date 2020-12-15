from selenium import webdriver
#import pyvirtualdisplay
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import re
import html5lib
from Student import Student

##Sorry for spaghetti, hardly works


driver = webdriver.Safari()
driver.get('https://pot.degreeworks.suny.edu/potDashboardServlet/dashboard')

sel = Select(driver.find_element_by_css_selector(".form-control"))
sel.select_by_visible_text("Potsdam")

form = driver.find_element_by_id('loginForm')
form.submit()

time.sleep(5)

##change these for login
user = raw_input("Enter Potsdam ID ('example201': ") + "@potsdam.edu"
passw = raw_input("Enter password: ")

form = driver.find_element_by_id('loginForm')
username = driver.find_element_by_name("UserName")
username.send_keys(user)
password = driver.find_element_by_name("Password")
password.send_keys(passw)

form.submit()

time.sleep(20)


driver.switch_to_frame(driver.find_element_by_name("frBodyContainer"))
driver.switch_to_frame(driver.find_element_by_name("frBody"))

soup = BeautifulSoup(driver.page_source, 'html5lib')

takes = set()
taken = []
for x in soup.find_all("td", class_="CourseAppliedDataDiscNum"):
    takes.add(x.text.replace(u'\xa0', u' ').encode('utf-8'))

for x in soup.find_all("td", class_="ClassesAppliedClasses"):
    takes.add(x.text.replace(u'\xa0', u' ').encode('utf-8'))

for z in takes:
    taken.append(z)
    
def getTaken():
    return taken

need_data = []
for x in soup.find_all("td", class_="RuleAdviceData"):
    for y in x.find_all("a"):
        z = y.text.split()
        if (len(z) <= 2):
            need_data.append(z)

needs = []

label = 'err'

for d in need_data:
    if len(d) == 2:
        for x in d:
            x = x.replace(u'\xa0', u' ').encode('utf-8')
        needs.append(d[0].encode('utf-8') + " " + d[1].encode('utf-8'))
        label = d[0].encode('utf-8')
    if len(d) == 1:
        needs.append(label + " " + d[0].encode('utf-8'))

def getNeeds():
    return needs

stu_data = []

for x in soup.find_all("td", class_="StuTableData"):
    stu_data.append(x.text.replace(u'\xa0', u' ').encode('utf-8'))

student_list = []

#For right now, only puts one student object into list
student_list.append(Student(stu_data[3], stu_data[0], taken, needs))

def getStudents():
    return student_list
        
        



        
        



