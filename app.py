from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('player_overall.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        movement_reactions=int(request.form['movement_reactions'])
        mentality_composure = int(request.form['mentality_composure'])
        attacking_short_passing=int(request.form['attacking_short_passing'])
        skill_ball_control=int(request.form['skill_ball_control'])
        passing=int(request.form['passing'])
        potential=int(request.form['potential'])
        dribbling=int(request.form['attacking_short_passing'])
        skill_long_passing=int(request.form['attacking_short_passing'])
        power_shot_power=int(request.form['attacking_short_passing'])
        mentality_vision=int(request.form['attacking_short_passing'])
        
        
        prediction=model.predict([[movement_reactions,mentality_composure,attacking_short_passing,
        skill_ball_control,passing,potential,dribbling,skill_long_passing,
        power_shot_power,mentality_vision]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you Predict for this")
        else:
            return render_template('index.html',prediction_text="Your Prediction is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)