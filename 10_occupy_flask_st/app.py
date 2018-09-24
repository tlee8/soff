#Cathy Cai and Thomas Lee - CaiLee
#SoftDev1 pd6
#K 10 -- Jinja Tuning
#2018-09-23

from flask import Flask, render_template
from octoquackers import makeDict, randOccupation, occupations
app = Flask(__name__)

@app.route('/')
    
def home():
    return '''<h3>Welcome to your future.</h3>
            <a href='/occupations'>Get started</a>
            '''

linkDict = {}
makeDict('occupations.csv', linkDict, 0, 2)

@app.route('/occupations')

def nothome():
    rOccupation = randOccupation()
    return render_template('/occupations.html',
                           collection=occupations,
                           randomOccupation=rOccupation,
                           occupationLink=linkDict[rOccupation]
                           )


if __name__ == '__main__':
    app.debug = True
    app.run()
