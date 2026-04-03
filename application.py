import pickle
from flask import Flask, render_template, request
import numpy as np

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('ridge_model.pkl', 'rb'))
standard_scaler = pickle.load(open('scaler.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    result = None

    if request.method == "POST":
        Tempreture = float(request.form.get('Tempreture'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data = standard_scaler.transform(
            [[Tempreture, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        )

        result = ridge_model.predict(new_data)[0]

    return render_template('home.html', results=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
