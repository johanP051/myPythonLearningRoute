from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home/")
def home():
    return "Estás en el home"

@app.route("/about/")
def about():
    return "<h1>This is the about</h1>"

@app.route("/notes/<string:name>/")
def notes(name):
    return f"<h1>Hola {name}</h1>"

@app.route("/testing")
def testing():
    return 2+2

#debug mode: ON
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)