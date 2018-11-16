#Thomas Lee
#SoftDev1 pd6
#K26 -- Getting More REST
#2018-11-15

import urllib, json, os

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/studio")
def studio():
    return render_template("studio.html")

@app.route("/ghibli")
def ghibli():
    numMovies = request.args['numMovies']
    if numMovies.isdigit():
        s = urllib.request.urlopen("https://ghibliapi.herokuapp.com/films?limit=" + str(numMovies))
        s = s.read()
        d = json.loads(s)
        return render_template("ghibli.html",films=d)
    else:
        flash ("You did not enter a number. Try again.")
        return redirect(url_for("studio")) 

            

@app.route("/dog")
def dog():
    url = "https://random.dog/woof.json"
    s = urllib.request.urlopen(url)
    s = s.read()
    d = json.loads(s)
 
    return render_template("dog.html", link = d['url'])

@app.route("/numbers")
def numbers():
    url = "http://numbersapi.com/random"
    s = urllib.request.urlopen(url)
    s = s.read()
    return render_template('numbers.html', info = str(s)[2:-1])

if __name__== "__main__":
    app.debug = True
    app.run()

