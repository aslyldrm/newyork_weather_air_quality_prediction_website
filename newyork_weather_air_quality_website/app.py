from flask import Flask, render_template, request
import pickle




app = Flask(__name__)


model = pickle.load(open("clf.pkl", "rb"))

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():

    name = int(request.form['name'])
    measure = int(request.form['measure'])
    geo_type_name = int(request.form['geo_type_name'])
    geo_place_name = int(request.form['geo_place_name'])
    time_period = int(request.form['time_period'])
    data_value = float(request.form['data_value'])

    model_input = [[name, measure, geo_type_name, geo_place_name, time_period, data_value]]


    prediction = model.predict(model_input)
  
    text = ""
    if prediction[0] =='Bad':
        text = "Bad"
    
    elif prediction[0] =='Moderate':
        text = "Moderate"
    else:
        text = "Good"
     
    return render_template("index.html", text=text)





if __name__=="__main__":
    app.run(debug=True)
    
    
    
