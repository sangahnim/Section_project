import numpy as np
import pickle
import joblib

from flask import Flask, request, jsonify, render_template
 
 
app = Flask(__name__)
# model = pickle.load(open('model.pkl','r'))

# main(home) page routing 
@app.route('/')
def home():
    return render_template('index.html')

# data predict processing
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    # features
    bpm_tempo = str(request.form['bpm_tempo'])
    energy = str(request.form['energy'])
    danceability = str(request.form['danceability'])
    decibel = str(request.form['decibel'])
    length = str(request.form['length'])
    speechiness = str(request.form['speechiness'])
    # speechiness = request.form.get['speechiness']

    final_features = np.array([[bpm_tempo, energy, danceability, decibel, length, speechiness]])
    #final_features = [np.array(float_features)]

    # 가져오기
    model = joblib.load('model.pkl','r')

    prediction = model.predict(final_features)
    
    output = prediction[0]
 
    return render_template('index.html', prediction_text='너의 음악 취향은 {}!!'.format(output))
 
'''@app.route('/results',methods=['POST'])
def results():
 
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
 
    output = prediction[0]
    return jsonify(output)'''

 
if __name__ == "__main__":
    app.run(debug=True)




