from flask import Flask, render_template, request, jsonify
import pickle
from src.logger import logging
from src.exception import CustomException

from sklearn.preprocessing import StandardScaler




application = Flask(__name__)

app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')
    
    else:
        data = Cust


if __name__ == "__main__":
    app.run(debug=True)
    