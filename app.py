from flask import Flask, jsonify, render_template, request
import numpy as np
from utils import prediction_heartDisease

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    print('final_features', final_features)
    output = prediction_heartDisease(final_features)
    print(output)
    if output == 1:
        return render_template('home.html', prediction_text='THE PATIENT IS LIKELY TO HAVE A HEART FAILURE')
    else:
        return render_template('home.html', prediction_text='THE PATIENT IS NOT LIKELY TO HAVE A HEART FAILURE')
app.run(debug=True)