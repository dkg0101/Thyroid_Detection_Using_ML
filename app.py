from flask import Flask, render_template, request, jsonify
import pickle
from src.logger import logging



app = Flask(__name__)


@app.route('/index', methods =['GET','POST'])
def index():
    return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=True)
    