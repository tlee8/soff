#Thomas Lee
#SoftDev1 pd6
#K 13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/")
def input():
    return render_template('input.html')

@app.route("/auth")
def auth():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    return render_template('authorize.html',
                           username = request.args['username'],
                           method = request.method
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
