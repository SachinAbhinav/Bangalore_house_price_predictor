from flask import Flask, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello Woriild"

@app.route('/get_locations', methods=['GET'])
def get_locations():
    response = jsonify({
        'locations': util.get_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['GET', 'POST'])
def predict_price():
    print(request.form, 'GHai')
    total_sqft = request.form['total_sqft']
    bhk = request.form['bhk']
    balcony = request.form['balcony']
    location = request.form['location']
    bath = request.form['bath']


    response = jsonify({
        # 'price': 10
        'predicted_price': util.predict_price(total_sqft, bhk, balcony, bath, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    app.run()