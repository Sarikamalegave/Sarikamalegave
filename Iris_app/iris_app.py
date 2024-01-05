from flask import Flask, render_template, request
import numpy as np
import pickle

with open("iris_model.pickle","rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction", methods=["post"])
def prediction():
    sepalL = float(request.form.get("sepalL"))
    sepalW = float(request.form.get("sepalW"))
    petalL = float(request.form.get("petalL"))
    petalW = float(request.form.get("petalW"))

    prediction_input = np.array([sepalL,sepalW,petalL,petalW])

    prediction_output = model.predict([prediction_input])[0]

    if prediction_output == 0:
        prediction_output = "Iris Setosa"
    elif prediction_output == 1:
        prediction_output = "Iris Versicolour"
    elif prediction_output == 2:
        prediction_output = "Iris Virginica"

    return prediction_output

if __name__ == "__main__":
    app.run(debug = True, port = 8080, host = "0.0.0.0")