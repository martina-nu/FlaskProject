from flask import Flask, render_template, jsonify, request 
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__) # hacer ref al nombre del archivo

@app.route('/')
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio')
def show_home():
    return "Hello World"
    
@app.route('/<string:country>/<string:variety>/<float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>')
def result(country,variety,aroma,aftertaste,acidity,body,balance,moisture):
    cols = ['country_of_origin','variety','aroma', 'aftertaste','acidity','body','balance','moisture']
    data = [country,variety,aroma,aftertaste,acidity,body,balance,moisture]
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
    loaded_model = pickle.load(open('coffee_model.pkl','rb'))
    result = loaded_model.predict(posted)
    text_result = result.tolist()[0]

    if text_result == 'Yes':
        return jasonify(message='Es un café de especialidad'),200
    else:
        return jasonify(message='No es un café de especialidad'),200

if __name__ == '__main__':
    app.run(debug= True, host='127.0.0.1', port=5000) 

