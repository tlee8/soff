from flask import Flask
app = Flask(__name__)

@app.route("/") 
def juice__world():
    print (__name__)
    return "<a href='/juice'> Juice Wrld </a>"

@app.route("/juice")
def lucid_dreams():
    print (__name__)
    return "<a href='/lyrics'> Lucid Dreams</a> by <a href='/'>Juice Wrld </a>"

@app.route("/lyrics")
def lyrics():
    print (__name__)
    return "I have these <a href='/juice'> lucid dreams</a> where I can't move a thing"

app.debug = True
app.run()
