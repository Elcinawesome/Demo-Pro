#Edit

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


with open('model_final' , 'rb') as f:
  model = pickle.load(f)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  if request.method == 'POST':
    
    
    SEX = int(request.form['SEX'])
    AGE_DX = int(request.form['AGE_DX'])
    GRADE = int(request.form['GRADE'])
    NO_SURG = int(request.form['NO_SURG'])
    RADIATN = int(request.form['RADIATN'])
    NUMPRIMS = int(request.form['NUMPRIMS'])
    FIRSTPRM = int(request.form['FIRSTPRM'])
    DTH_CLASS = int(request.form['DTH_CLASS'])
    ERSTATUS = int(request.form['ERSTATUS'])
    PRSTATUS = int(request.form['PRSTATUS'])
              
    data = np.array([[SEX, AGE_DX, GRADE, NO_SURG, RADIATN, NUMPRIMS,
      FIRSTPRM, DTH_CLASS, ERSTATUS, PRSTATUS]])
    output = model.predict(data)
    if output == 0:
        res_val = "DEAD"
    elif output == 1:
        res_val = "ALIVE"
      
    return render_template('index.html', prediction_text='Patient will be {}'.format(res_val))
#  input_features = [int(x) for x in request.form.values()]
#  features_value = [np.array(input_features)]
#
#  features_name = ['AGE_DX', 'GRADE', 'NO_SURG', 'RADIATN', 'FIRSTPRM']
#
#  df = pd.DataFrame(features_value, columns=features_name)
#  output = model.predict(df)
#  print(df)
#
#  if output == 0:
#      res_val = "DEAD"
#  if output == 1:
#      res_val = "ALIVE"
#  else:
#    res_val = "Problem with input"


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
  
