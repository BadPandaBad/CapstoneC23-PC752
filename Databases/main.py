from flask import Flask, request make_response, jsonify
from PIL import image
impport os
from code_capstone import

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':

if __name__ == '__main__':
    app.run()