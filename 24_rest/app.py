#Thomas Lee
#SoftDev1 pd6
#K24 --  A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def rest():
    url = "https://api.nasa.gov/planetary/apod?api_key=54FEbz3y1Hlprqa74pXDAQlA7mfqlrwCOlsTVK6D"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    return render_template("index.html", link = d['url'])

if __name__== "__main__":
    app.debug = True
    app.run()
