#Thomas Lee
#SoftDev1 pd6
#K25 -- Getting More REST
#2018-11-14

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

@app.route("/cat")
def cat():
    url = "https://aws.random.cat/meow"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
    print (d)
    return render_template("cat.html", link = d['file'])



if __name__== "__main__":
    app.debug = True
    app.run()
