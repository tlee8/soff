#Mohammed A Lee - Mohammed Uddin and Thomas Lee
#SoftDev1 pd6
#K15 -- Oh yes, perhaps I do…
#2018-10-02
from flask import Flask, render_template, request, session, url_for, redirect,flash
import os

app = Flask(__name__)


app.secret_key = os.urandom(32)   #super secret key hidden under the doormat

#hardcoded login
user = 'abc'
pw = '123'

@app.route("/")
def login():
    if "username" in session:      #if you're logged in already, just go to the welcome page
        return render_template('welcome.html', username= session['username'])
    return render_template('login.html')  #otherwise login

@app.route("/auth")
def logged():
    if request.args['username'] == user and request.args['password'] == pw:        #if you have the right credentials
        session['username'] = request.args['username']                             #you get to join the super secret club
        return render_template('welcome.html', username= request.args['username'])
    else:
        flash ('Invalid Login. Please Try Again.')
        return redirect(url_for("login")) 
       # return render_template('error.html')
       #otherwise you get kicked out

@app.route("/exit")
def leave():
    session.pop('username')                   #you've chosen to leave and head out into the dangerous world
    return redirect(url_for("login"))         #but you soon come to reget your decision and come back to the login page


if __name__== "__main__":
    app.debug = True
    app.run()
