from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def button():
    return render_template(
        'button.html'
        )

@app.route("/auth"):
def authenticate ():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.header)
    return "Waaaa hooo HAAAH"

if __name__== "__main__":
    app.debug = True
    app.run()
