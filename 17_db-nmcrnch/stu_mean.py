#Matthew Ming and Thomas Lee - Ming Dynasty
#SoftDev1 pd06
#K 17 -- Average
#2018 - 10 - 07

import sqlite3
from db_builder import *
db = sqlite3.connect("discobandit.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def stu_meaner(list1,list2):
    c.execute("DROP TABLE IF EXISTS peeps_avg;")#removes existing table, otherwise creates
    c.execute("CREATE TABlE peeps_avg (id TEXT, avg TEXT)")
    idlist = list(c.execute( "SELECT id FROM "+list1))#assembles all ids
    id_list = []
    for el in idlist:
        id_list.append(el[0])
    for ide in id_list:
        print ("==========================================" + "\n")
        command = "SELECT name FROM {} WHERE id = ".format(list1)#matches names to id
        command += ide
        name = (list(c.execute(command))[0][0])
        print (name)
        print (ide)
        command = "SELECT mark FROM {} WHERE id = ".format(list2)#gets grades from id
        command += ide
        gradelist = []
        gradelist = list(c.execute (command))
        #print (gradelist)
        grade_list = []
        for el in gradelist:
            grade_list.append(int(el[0]))
        #print (grade_list)
        avg = 0
        avg = str(sum(grade_list) / len(grade_list))#calculates avg for each person
        print (avg + "\n")
        params = (ide, avg)
        c.execute("INSERT INTO peeps_avg VALUES (?,?)", params) #adds avgs and ids to peeps_avg
        '''
        command = "INSERT INTO peeps_avg VALUES("
        command += ide + ", "
        command += avg
        command += ")"
        #print(command)
        c.execute(command)
        '''
        
def addRowToCourses(code,mark,id_num):
    command = "INSERT INTO course_list VALUES(?,?,?)"#adds a new row with these values
    c.execute(command,(code,mark,id_num)) 
stu_meaner("peep_list","course_list")
addRowToCourses("systems",95,2)
addRowToCourses("softdev",60,5)
addRowToCourses("ai",75,9)
print("==================NEW TABLE=============")
stu_meaner("peep_list","course_list")
db.commit()
db.close()
