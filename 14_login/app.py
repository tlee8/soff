from flask import Flask, render_template, request, session
import os
app = Flask(__name__)

@app.route("/")
def login():
    if session.pop("abc")==("123"):
        return redirect(url_for('logged'))
    return render_template('login.html')
i
@app.route("/auth")
def logged():
    if request.args["username"] == "abc" and request.args["password"] == "123":
        session['abc'] = '123'
        return "good" #render_template('good.html')
    else:
        return "bad" #render_template('bad.html')

if __name__== "__main__":
    app.debug = True
    app.run()
