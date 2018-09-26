#Cathy Cai and Thomas Lee - CaiLee
#SoftDev1 pd6
#K11 -- Jinja Tuning
#2018-09-23

from flask import Flask, render_template
from util import octoquackers #allows us to import our occupations functions and csv file with the percentages
app = Flask(__name__)

@app.route('/')

#Generates a homepage with a link to our occupations page
def home():
    return '''<h3>Welcome to your future.</h3>
            <a href='/occupations'>Get started</a> 
            '''

#makes a dictionary that holds all the occupations with its respective percentages
occupationsDict = {}
octoquackers.makeDict(r'data/occupations.csv', occupationsDict, 0, 1)

#makes a dictionary that holds all the occupations with its respective links
linkDict = {}
octoquackers.makeDict(r'data/occupations.csv', linkDict, 0, 2) 

@app.route('/occupations')

def nothome():
    #Generates a random occupation based on the given percentage 
    rOccupation = octoquackers.randOccupation(occupationsDict)

    #accesses the html file within the 'templates' folder
    return render_template('/occupations.html',

                           #assign variables that are used in the html file
                           collection=occupationsDict, 
                           links=linkDict,
                           randomOccupation=rOccupation,
                           occupationLink=linkDict[rOccupation] #link associated with that random occupation
                           )


if __name__ == '__main__':
    app.debug = True
    app.run()
