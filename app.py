from flask import Flask, request, jsonify
import boto3
import json

app = Flask(__name__)

def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -payments)
    return monthly_payment

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    principal = data.get('principal')
    annual_rate = data.get('annual_rate')
    years = data.get('years')

    if not all([principal, annual_rate, years]):
        return jsonify({'error': 'Missing data'}), 400

    monthly_payment = calculate_mortgage(principal, annual_rate, years)
    return jsonify({'monthly_payment': monthly_payment})

if __name__ == '__main__':
    app.run(debug=True)
