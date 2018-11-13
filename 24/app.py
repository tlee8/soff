#smilesAndSilence -- Britni Canale && Thomas Lee
#SoftDev1 pd6
#K24 --  A RESTful Journey Skyward
#2018-11-13

from flask import Flask
import urllib, json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", url = url)

if __name__== "__main__":
    app.debug = True
    app.run()
