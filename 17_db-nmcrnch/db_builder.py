#Matthew Ming and Thomas Lee - Ming Dynasty 
#SoftDev1 pd06
#K 17 -- Average
#2018 - 10 - 07

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect("discobandit.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

#command = db.cursor()          #build SQL stmt, save as string

def course_reader():
    c.execute("DROP TABLE IF EXISTS course_list;")
    c.execute("CREATE TABLE course_list (code TEXT, mark TEXT, id TEXT)")    #run SQL statement
    with open ('courses.csv', "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            code = row['code']
            mark = row['mark']
            id = row['id']
            command = "INSERT INTO course_list VALUES("
            command += "'" + code + "', "
            command += mark + ", "
            command += id
            command += ")"
            #print(command)
            c.execute(command)

def peep_reader():
    c.execute("DROP TABLE IF EXISTS peep_list;")
    c.execute("CREATE TABLE peep_list (name TEXT, age TEXT, id TEXT)")    #run SQL statement
    with open ('peeps.csv', "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            age = row['age']
            id = row['id']
            command = "INSERT INTO peep_list VALUES("
            command += "'" + name + "', "
            command += age + ", "
            command += id
            command += ")"
            #print(command)
            c.execute(command)


#==========================================================
course_reader()
peep_reader()


db.commit() #save changes
db.close()  #close database

