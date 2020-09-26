from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if request.form['drive-wheels'] == 'rwd':
        drive_wheels = 0
    elif request.form['drive-wheels'] == 'fwd':
        drive_wheels = 1 
    elif request.form['drive-wheels'] == '4wd':
        drive_wheels = 2        
    wheel_base =  request.form['wheel-base']
    length =  request.form['length']
    width =  request.form['width']
    curb_weight =  request.form['curb-weight']
    if request.form['num-of-cylinders'] == 'four':
        num_of_cylinders = 4
    elif request.form['num-of-cylinders'] == 'six':
        num_of_cylinders = 6 
    elif request.form['num-of-cylinders'] == 'five':
        num_of_cylinders = 5        
    elif request.form['num-of-cylinders'] == 'three':
        num_of_cylinders = 3        
    elif request.form['num-of-cylinders'] == 'twelve':
        num_of_cylinders = 12        
    elif request.form['num-of-cylinders'] == 'two':
        num_of_cylinders = 2        
    elif request.form['num-of-cylinders'] == 'eight':
        num_of_cylinders = 8
    engine_size =  request.form['engine-size']
    bore =  request.form['bore']
    horsepower =  request.form['horsepower']
    city_lper100km =  request.form['city-l/100km']
    highway_lper100km =  request.form['highway-l/100km']
    x_test = [[drive_wheels,wheel_base,length,width,curb_weight,num_of_cylinders,engine_size,bore,horsepower,city_lper100km,highway_lper100km]]            
    result = model.predict(scaler.transform(x_test))[0]
    return render_template("index.html", result=result)    

if __name__ == "__main__":
    app.run()    