import json

def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -payments)
    return monthly_payment

def lambda_handler(event, context):
    data = json.loads(event['body'])
    principal = data.get('principal')
    annual_rate = data.get('annual_rate')
    years = data.get('years')

    if not all([principal, annual_rate, years]):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing data'})
        }

    monthly_payment = calculate_mortgage(principal, annual_rate, years)
    return {
        'statusCode': 200,
        'body': json.dumps({'monthly_payment': monthly_payment})
    }
