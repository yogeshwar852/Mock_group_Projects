import json, pickle
import numpy as np

model = pickle.load(open('./artifacts/heart_disease_pred.pickle','rb'))
columns = json.load(open('./artifacts/columns.json','r'))['columns']

features =  [np.array(columns)]
print("features in utils.py",features)
def prediction_heartDisease(features):
    
    prediction = model.predict(features)
    return round(prediction[0],2)