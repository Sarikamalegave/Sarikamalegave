from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/test_route")

def test_function():
    return "We are testing a new function!"

@app.route("/test_html")
def test_html():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug = True, port=8080,host="0.0.0.0")