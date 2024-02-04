from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

@app.route("/")
def index(): 
    # when getting prediction from route "/predict"
    prediction = request.args.get("prediction") 
    sl = request.args.get("sl")
    sw = request.args.get("sw")
    pl = request.args.get("pl")
    pw = request.args.get("pw")

    data = {"sepal_length": sl, 
            "sepal_width": sw, 
            "petal_length": pl, 
            "petal_width": pw}
     
    return render_template('index.html', prediction=prediction, data=data)

@app.route("/predict", methods=["POST"])
def predict(): 
    data = request.form
    
    sepal_length = float(data.get("sepal_length"))
    sepal_width = float(data.get("sepal_width"))
    petal_length = float(data.get("petal_length"))
    petal_width = float(data.get("petal_width"))

    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    
    with open('model.pkl', 'rb') as file: 
        model = pickle.load(file)

    target_names = ['setosa', 'versicolor', 'virginica']
    prediction = target_names[model.predict(input_data)[0]]
    
    return redirect(url_for('index', prediction=prediction, sl=sepal_length, sw=sepal_width, pl=petal_length, pw=petal_width))



if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=8080)